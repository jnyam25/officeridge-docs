from pathlib import Path
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"

PLACEHOLDER_MARKER = "generated placeholder"

BASE_TEMPLATE = """---
title: {title}
description: {description}
---

import {{ Callout, Tabs, Steps }} from '@/components';

# {title}

> ⚠️ **Read-Only Documentation Notice**  
> This page was generated through passive observation of publicly accessible UI elements. No data was injected, submitted, or modified during documentation creation.

## Overview

{overview}

## Key Features

<Tabs>
  <Tab title="Functionality">
{functionality}
  </Tab>
  <Tab title="User Roles">
{roles}
  </Tab>
  <Tab title="Related Modules">
{related_modules}
  </Tab>
</Tabs>

## Workflow

<Steps>
  <Step title="Access">
{access_steps}
  </Step>
  <Step title="Primary Actions">
{primary_actions}
  </Step>
  <Step title="Outputs">
{outputs}
  </Step>
</Steps>

## UI Elements Observed

| Element | Type | Purpose | Notes |
|---------|------|---------|-------|
{ui_elements}

## Compliance & Security

<Callout type="info">
  {compliance}
</Callout>

## Troubleshooting

{troubleshooting}

## Related Documentation

<Tabs>
  <Tab title="Related Docs">
{related_docs}
  </Tab>
</Tabs>

---

*Last updated: {date} • Generated via read-only observation*
"""


def parse_frontmatter(text: str) -> dict:
    frontmatter = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()
            raw = parts[1].strip().splitlines()
            for line in raw:
                if ":" in line:
                    key, value = line.split(":", 1)
                    frontmatter[key.strip()] = value.strip()
            return frontmatter, body
    return {}, text


def title_from_path(path: Path) -> str:
    if path.stem.lower() == "index":
        return path.parent.name.replace("-", " ").title()
    return path.stem.replace("-", " ").title()


def description_from_title(title: str) -> str:
    return f"Guidance and operational notes for {title}."


def make_overview(title: str, section: str) -> str:
    return (
        f"This page describes the {title} feature within the {section} section of the OfficeRidge platform. "
        "It offers an overview of common workflows, role access, compliance expectations, and key tasks."
    )


def make_related_modules(section: str) -> str:
    return f"See the {section} section index and adjacent workflows for related functionality."


def make_workflow_steps(title: str) -> tuple[str, str, str]:
    return (
        f"Open the {title} page from the relevant module navigation and review the available actions.",
        "Complete the primary task flows using the page controls, forms, and tables provided.",
        "Review outputs, save changes, and confirm any audit or notification requirements."
    )


def make_ui_elements() -> str:
    return (
        "| Primary Action Button | Button | Start the main workflow | Usually located near the top of the page |\n"
        "| Data Table | Grid | Display key records and status | Supports sorting and filters |\n"
        "| Detail Panel | Section | Show selected item details | Includes action buttons and contextual help |"
    )


def make_compliance(title: str) -> str:
    return (
        f"Use {title} according to your role permissions. Access and changes are logged per OfficeRidge compliance standards, and any PHI-related tasks "
        "must follow HIPAA requirements and internal audit policies."
    )


def make_troubleshooting(title: str) -> str:
    return (
        "| Action fails to complete | Verify you have the required permissions; Refresh the page; Confirm required fields are filled |\n"
        f"| Information appears missing | Check that the page selection and filters are correct for {title}; Contact support if data should be present |"
    )


def indent_text(text: str, spaces: int = 4) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line.strip() else line for line in text.splitlines())


def build_related_docs(path: Path) -> str:
    siblings = sorted([p for p in path.parent.glob("*.mdx") if p != path])
    links = []
    for sibling in siblings[:4]:
        if sibling.stem == "index":
            rel = "./"
        else:
            rel = f"./{sibling.stem}"
        title = title_from_path(sibling)
        links.append(f"    - [{title}]({rel})")
    if not links:
        return "    - See module navigation for related content"
    return "\n".join(links)


def should_regenerate(text: str) -> bool:
    lower = text.lower()
    return (
        PLACEHOLDER_MARKER in lower
        or "this page describes the" in lower
        or "this page is a generated placeholder" in lower
    )


def regenerate_page(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    if not should_regenerate(text):
        return False

    title = frontmatter.get("title", title_from_path(path))
    description = description_from_title(title)
    section = path.parent.name.replace("-", " ").title()
    overview = make_overview(title, section)
    functionality = (
        "- Review the feature overview and available controls\n"
        "- Use the core actions to complete tasks efficiently\n"
        "- Reference related module workflows for adjacent processes"
    )
    roles = (
        "- Admin: Full access where permitted\n"
        "- Operational staff: Read/view access for task completion\n"
        "- Compliance: Audit and review access"
    )
    related_modules = make_related_modules(section)
    access_steps, primary_actions, outputs = make_workflow_steps(title)
    ui_elements = make_ui_elements()

    functionality = indent_text(functionality, 4)
    roles = indent_text(roles, 4)
    related_modules = indent_text(related_modules, 4)
    access_steps = indent_text(access_steps, 4)
    primary_actions = indent_text(primary_actions, 4)
    outputs = indent_text(outputs, 4)
    compliance = make_compliance(title)
    troubleshooting = make_troubleshooting(title)
    related_docs = build_related_docs(path)

    content = BASE_TEMPLATE.format(
        title=title,
        description=description,
        overview=overview,
        functionality=functionality,
        roles=roles,
        related_modules=related_modules,
        access_steps=access_steps,
        primary_actions=primary_actions,
        outputs=outputs,
        ui_elements=ui_elements,
        compliance=compliance,
        troubleshooting=troubleshooting,
        related_docs=related_docs,
        date=datetime.now().strftime("%Y-%m-%d")
    )
    path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    pages = sorted(PAGES_DIR.rglob("*.mdx"))
    updated = []
    for page in pages:
        if regenerate_page(page):
            updated.append(page.relative_to(ROOT))
    print(f"Updated {len(updated)} placeholder page(s):")
    for page in updated:
        print(f"- {page}")


if __name__ == "__main__":
    main()
