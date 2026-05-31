"""
Mintlify Page Generator for OfficeRidge
Generates .mdx files from template using module structure data
"""

import os
from pathlib import Path
from datetime import datetime
# generator.py
from modules_data import MODULES, BASE_TEMPLATE
from pathlib import Path

def generate_page(module: str, subgroup: str, page_key: str, data: dict, output_dir: Path):
    """Generate a single .mdx page"""
    content = BASE_TEMPLATE.format(**data)
    
    # Create path: pages/{module}/{subgroup}/{page_key}.mdx
    if subgroup == "index":
        page_path = output_dir / module / f"{page_key}.mdx"
    else:
        page_path = output_dir / module / subgroup / f"{page_key}.mdx"
    
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(content, encoding='utf-8')
    print(f"✓ Generated: {page_path}")

def main():
    output_dir = Path("pages")
    
    for module_name, submodules in MODULES.items():
        for subgroup_name, pages in submodules.items():
            for page_key, page_data in pages.items():
                generate_page(module_name, subgroup_name, page_key, page_data, output_dir)
    
    print(f"\n🎉 Generated {sum(len(p) for s in MODULES.values() for p in s.values())} pages!")

if __name__ == "__main__":
    main()
# Base template with placeholder replacement
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
    {related}
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
{ui_table}

## Compliance & Security

<Callout type="info">
  {compliance}
</Callout>

## Troubleshooting

{troubleshooting}

## Related Documentation

{related_links}

---

*Last updated: {date} • Generated via read-only observation*
"""

# Module structure data (expand as needed)
MODULES = {
    "members": {
        "member-directory": {
            "authorizations": {
                "title": "Authorizations",
                "description": "Track payer approvals, coverage limits, and renewal dates",
                "overview": "Manage insurance authorizations, Medicaid waivers, and private pay approvals for member services.",
                "functionality": "- Verify coverage eligibility\n- Track authorization expiration dates\n- Upload supporting documentation\n- Set renewal reminders",
                "roles": "- Admin: Full CRUD\n- Billing: Read + Update\n- Clinical: Read-only",
                "related": "Member Directory, Claims & Billing, Payer Management",
                "access_steps": "Navigate to Members → Member Directory → Select member → Authorizations tab",
                "primary_actions": "Search authorizations by payer/date; Upload new approval letters; Flag expiring items",
                "outputs": "Authorization status report; Expiration alert list; Payer compliance summary",
                "ui_table": "| Authorization Status Badge | Visual indicator | Show approval state | Green=Active, Yellow=Expiring Soon, Red=Expired |\n| Payer Filter Dropdown | Selection control | Filter by insurance provider | Includes Aetna, BCBS, Cigna, Medicaid, Medicare |",
                "compliance": "Authorization data is PHI-adjacent. Access logged per HIPAA. Export requires 'Billing Export' role permission.",
                "troubleshooting": "| Authorization not visible | Verify member is assigned to your caseload; Check payer contract status in Licensing module |",
                "related_links": "- [Member Directory](/members/member-directory)\n- [Payer Management](/licensing/payer-management)\n- [Claims Upload](/claims-billing/upload-claims)"
            },
            # Add more sub-pages here following same pattern
        },
        "care-and-assessment": {
            "care-plans": {
                "title": "Care Plans",
                "description": "Create, update, and track individualized member care plans",
                "overview": "Develop comprehensive care plans aligned with physician orders, member goals, and regulatory requirements.",
                "functionality": "- Template-based plan creation\n- Goal tracking with measurable outcomes\n- Interdisciplinary team collaboration\n- Version history and audit trail",
                "roles": "- Clinical Staff: Create/Edit\n- Management: Approve\n- Admin: Full access",
                "related": "Risk Assessments, Physician Orders, Discharge Planning",
                "access_steps": "Members → Care and Assessment → Care Plans → Select member or 'New Plan'",
                "primary_actions": "Select care plan template; Define goals with metrics; Assign responsible staff; Set review dates",
                "outputs": "Printable care plan PDF; Goal progress dashboard; Compliance report for surveys",
                "ui_table": "| Goal Progress Tracker | Visual widget | Show completion % | Auto-updates from service logs |\n| Team Assignment Panel | Multi-select | Assign care team members | Shows role and contact info |",
                "compliance": "Care plans are legal documents. All edits require electronic signature. Changes trigger audit log entries with before/after values.",
                "troubleshooting": "| Template missing | Verify module license includes care planning; Contact admin for template library access |",
                "related_links": "- [Risk Assessments](/members/care-and-assessment/risk-assessments)\n- [Physicians](/members/care-and-assessment/physicians)\n- [Discharge Planning](/members/care-and-assessment/discharge-planning)"
            }
        }
    },
    "employees": {
        "background-checks": {
            "federal-oig": {
                "title": "Federal OIG Checks",
                "description": "Screen staff against federal exclusion lists",
                "overview": "Automated screening of employees and contractors against the HHS Office of Inspector General List of Excluded Individuals/Entities (LEIE).",
                "functionality": "- Bulk upload staff identifiers\n- Scheduled re-screening (monthly/quarterly)\n- Alert on new exclusions\n- Documentation for audit trails",
                "roles": "- HR/Compliance: Full access\n- Management: Read + Alert config\n- Others: No access",
                "related": "State OIG, DPS Checks, Drug Screening",
                "access_steps": "Employees → Background Checks → Federal OIG tab",
                "primary_actions": "Upload CSV of staff IDs; Configure screening frequency; Review match results; Document resolution",
                "outputs": "Screening completion report; Exclusion match alert; Compliance attestation document",
                "ui_table": "| Match Status Indicator | Visual badge | Show screening result | Green=Clear, Red=Match, Yellow=Pending Review |\n| Resolution Workflow | Guided form | Document investigation steps | Required fields for compliance |",
                "compliance": "OIG screening is required for Medicaid/Medicare providers. All screenings and resolutions must be documented per 42 CFR §1001. Records retained 10 years.",
                "troubleshooting": "| Upload fails | Verify CSV format matches template; Check file size <10MB; Ensure no special characters in names |",
                "related_links": "- [State OIG](/employees/background-checks/state-oig)\n- [DPS Checks](/employees/background-checks/dps-checks)\n- [Compliance Checklists](/operations/hipaa-compliance/compliance-checklists)"
            }
        }
    }
    # Expand with all remaining modules following same pattern
}

def generate_page(module_path: str, page_key: str, page_data: dict, output_dir: Path):
    """Generate a single .mdx page from template and data"""
    content = BASE_TEMPLATE.format(
        title=page_data["title"],
        description=page_data["description"],
        overview=page_data["overview"],
        functionality=page_data["functionality"],
        roles=page_data["roles"],
        related=page_data["related"],
        access_steps=page_data["access_steps"],
        primary_actions=page_data["primary_actions"],
        outputs=page_data["outputs"],
        ui_table=page_data["ui_table"],
        compliance=page_data["compliance"],
        troubleshooting=page_data["troubleshooting"],
        related_links=page_data["related_links"],
        date=datetime.now().strftime("%Y-%m-%d")
    )
    
    # Create directory structure
    page_path = output_dir / module_path / f"{page_key}.mdx"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write file
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Generated: {page_path}")

def main():
    output_dir = Path("pages")
    
    for module, submodules in MODULES.items():
        for subgroup, pages in submodules.items():
            for page_key, page_data in pages.items():
                module_path = f"{module}/{subgroup}"
                generate_page(module_path, page_key, page_data, output_dir)
    
    print(f"\n🎉 Generation complete! Review files in {output_dir}/")

if __name__ == "__main__":
    main()