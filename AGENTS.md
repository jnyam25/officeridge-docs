---
title: AI Agent Guidelines
description: Operational guidelines for AI agents interacting with the OfficeRidge documentation system
---

# AI Agent Guidelines

> ⚠️ **Read-Only Documentation Notice**  
> This page was generated through passive observation of publicly accessible UI elements. No data was injected, submitted, or modified during documentation creation.

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com) for the **OfficeRidge Enterprise Healthcare Management Platform**
- Pages are MDX files with YAML frontmatter stored in `pages/`
- Configuration lives in `mint.json` (or `docs.json` per deployment)
- Use the Mintlify MCP server `https://mcp.mintlify.com` to edit content and settings via MCP
- Use the Mintlify docs MCP server `https://www.mintlify.com/docs/mcp` to query information about using Mintlify via MCP

## Terminology

{/* Healthcare platform-specific terms and preferred usage */}

| Term | Preferred Usage | Avoid | Context |
|------|----------------|-------|---------|
| **Member** | Healthcare recipient/patient | User, Customer, Client | HIPAA-compliant terminology for individuals receiving care |
| **Service Provider** | Employee, contractor, or volunteer delivering care | Staff, Worker, User | Encompasses all credentialed care personnel |
| **Agency** | The home healthcare organization | Company, Business, Entity | Regulatory term used in licensing and CMS documentation |
| **Care Plan** | Individualized clinical plan of care | Treatment Plan, Service Plan | CMS-aligned terminology for home health |
| **EVV** | Electronic Visit Verification | Time Tracking, Clock-in System | Federal requirement for Medicaid personal care services |
| **PHI** | Protected Health Information | Personal Data, Medical Records | HIPAA-defined term for regulated health information |
| **Authorization** | Payer approval for services | Pre-approval, Permission | Insurance/billing industry standard term |
| **Orientation** | Structured onboarding process | Training, Introduction | Distinct from ongoing competency/education activities |

{/* Additional terminology guidance */}
- Use **role-based language**: "Clinical staff," "Billing team," "Compliance officer" instead of generic "users"
- Reference **regulatory sources explicitly**: "per 42 CFR §484.55" not "per regulations"
- Distinguish **modules vs. features**: "Members module" contains "Member Directory feature"

## Style preferences

{/* Project-specific style rules for AI-generated content */}

### Voice & Tone
- Use **active voice** and **second person** ("you") for procedural content
- Use **third person** for compliance, security, and architectural documentation
- Maintain **professional, precise tone** — avoid colloquialisms, humor, or subjective language
- Default to **concise sentences**: one idea per sentence, max 25 words

### Formatting Standards
- **Headings**: Sentence case, no trailing punctuation (`## Care plan workflows` not `## Care Plan Workflows.`)
- **UI elements**: Bold for clickable items (`Click **Save**`), code formatting for fields (`Enter value in \`member_id\``)
- **File paths & commands**: Inline code with backticks (`mint.json`, `mintlify dev`)
- **Code blocks**: Specify language, include comments for enterprise safeguards:
  ````mdx
  ```javascript
  // SOC2: Log all data access attempts
  const auditLog = await logAccess({ userId, resource, action });


### Compliance-First Writing
- **Always include read-only disclaimer** on generated pages (see template)
- **Explicitly state regulatory alignment**: "Supports CMS CoPs §484.50" not "Helps with compliance"
- **Document access controls**: Note role-based restrictions for every workflow
- **Flag PHI handling**: Clearly mark sections containing or referencing protected health information

### Linking & Cross-References
- Use **relative paths** for internal links: `[Care Plans](/members/care-and-assessment/care-plans)`
- **Anchor links** for section jumps: `[Troubleshooting](#troubleshooting)`
- **External links** open in new tab with `rel="noopener"`: `[CMS Guidelines](https://cms.gov){:target="_blank" rel="noopener"}`

## Content boundaries

{/* Define what AI agents should and shouldn't document */}

### ✅ Document These
- **Public UI workflows**: Navigation, tab structures, visible form fields, observable outputs
- **Role-based access patterns**: Which roles can see/do what (based on UI visibility)
- **Compliance touchpoints**: Where HIPAA, CMS, state licensing requirements manifest in UI
- **Integration points**: Observable connections to EVV, payer APIs, external systems
- **Error states & validation**: Visible error messages, required field indicators, loading states
- **Export/reporting capabilities**: Available formats, filters, and access permissions

### ❌ Do Not Document
- **Authentication mechanics**: Password policies, MFA setup, session management internals
- **API endpoints or payloads**: Unless explicitly published in public API documentation
- **Database schemas or internal data models**: Even if inferable from UI behavior
- **Security configurations**: Firewall rules, encryption keys, audit log storage details
- **Internal admin tools**: Features only visible to super-admin or engineering roles
- **Pricing, billing logic, or contract terms**: Unless published in public resources
- **Speculative functionality**: Features observed in development/staging but not production

### ⚠️ Handle With Care
- **PHI examples**: Never use real member names, MRNs, or identifiable data. Use `[REDACTED]` or synthetic examples like `Member_12345`
- **Credential examples**: Never show real API keys, passwords, or tokens. Use `<YOUR_API_KEY>` placeholders
- **Regulatory interpretations**: State observable compliance features; avoid legal advice ("Consult your compliance officer for...")
- **Third-party service details**: Describe observable integrations; link to vendor docs for implementation specifics

## Agent operational constraints

{/* Mandatory constraints for all AI-generated documentation */}

### Strict Read-Only Protocol
```md
✅ ALLOWED:
- Read publicly accessible UI content
- Document visible navigation, tabs, workflows
- Capture screenshots of non-sensitive UI elements (no PHI)
- Describe observable functionality without interaction

❌ PROHIBITED:
- Submit forms, login credentials, or API requests
- Create, update, or delete any platform data
- Trigger workflows, notifications, or background jobs
- Access authentication-protected endpoints without credentials
- Modify configuration, settings, or user roles
```

### Data Handling Requirements
- **No PHI in examples**: All member/employee examples must use synthetic data
- **Redact sensitive values**: Replace real IDs, names, dates with `[REDACTED]` or pattern examples (`MRN: XXX-XX-1234`)
- **Watermark generated content**: Include generation timestamp and agent identifier in page footer
- **Audit trail**: Log all documentation generation sessions with scope and constraints applied

### Compliance Validation Checklist
Before publishing any agent-generated page:
```md
- [ ] Read-only disclaimer present in frontmatter and body
- [ ] No placeholder text (`{{...}}`, `[TODO]`) remains
- [ ] All internal links resolve (run `mintlify broken-links`)
- [ ] Screenshots (if any) contain no PHI and have descriptive alt text
- [ ] Role-based access notes match observed UI behavior
- [ ] Compliance sections reference specific regulations (CMS, HIPAA, state)
- [ ] Synthetic data examples follow redaction standards
- [ ] Page footer includes generation metadata and review date
```

## MCP server usage

{/* Guidance for agents using Mintlify MCP endpoints */}

### Connecting to Mintlify MCP
```javascript
// Example: Initialize MCP client for documentation updates
import { Client } from '@modelcontextprotocol/sdk/client';

const mcpClient = new Client({
serverUrl: 'https://mcp.mintlify.com',
auth: { type: 'bearer', token: process.env.MINTLIFY_MCP_TOKEN }
});

// Verify connection before operations
await mcpClient.ping();
```

### Safe Operations via MCP
```javascript
// ✅ SAFE: Read page content for analysis
const pageContent = await mcpClient.readPage({
path: '/members/care-and-assessment/care-plans'
});

// ✅ SAFE: Update non-sensitive metadata
await mcpClient.updateFrontmatter({
path: '/agents',
updates: { lastReviewed: new Date().toISOString() }
});

// ❌ UNSAFE: Never use MCP to inject user data or trigger workflows
// await mcpClient.submitForm({ ... }); // PROHIBITED
```

### Querying Mintlify Documentation
```javascript
// Use docs MCP server for platform guidance
const docsClient = new Client({
serverUrl: 'https://www.mintlify.com/docs/mcp'
});

// Example: Get MDX component reference
const componentDocs = await docsClient.query({
question: 'How do I use the <Tabs> component in MDX?'
});
```

### Error Handling & Fallbacks
```javascript
try {
await mcpClient.updatePage({ path, content });
} catch (error) {
// Log error with context but never expose internals
console.error(`Documentation update failed for ${path}: ${error.code}`);

// Fallback: Queue for human review instead of retrying blindly
await queueForReview({ path, content, error: error.code });
}
```

## Review & approval workflow

{/* Process for validating agent-generated documentation */}

1. **Agent Generation**: AI creates draft `.mdx` file using `BASE_TEMPLATE` and `MODULES` data
2. **Automated Validation**: CI pipeline runs:
 ```bash
 mintlify broken-links
 grep -r "{{" pages/ && exit 1  # Fail on placeholders
 grep -r "Read-Only Documentation Notice" pages/ | wc -l  # Verify coverage
 ```
3. **Compliance Spot-Check**: Designated reviewer validates:
 - PHI redaction standards
 - Regulatory reference accuracy
 - Role-based access descriptions
4. **Human Approval**: Required for:
 - New module documentation
 - Changes to compliance/security sections
 - Pages with >3 major content revisions
5. **Publication**: Approved pages merged to `main` and deployed via Mintlify

## Agent identity & attribution

{/* Required metadata for agent-generated content */}

Every agent-generated page must include in frontmatter:
```yaml
---
generatedBy: "agent-id-xyz"
generatedAt: "2026-01-15T10:30:00Z"
reviewedBy: "human-reviewer-id" # Populated post-approval
reviewedAt: "2026-01-15T14:22:00Z" # Populated post-approval
constraintsApplied:
- read-only-mode
- phi-redaction
- compliance-validation
---
```

And in page footer:
```md
---
*Generated by [Agent ID] on {{generatedAt}} • Reviewed {{reviewedAt}} • Next review: Quarterly*
```

---

> ℹ️ **Maintenance Note**: This document should be reviewed quarterly alongside SOC2/GDPR compliance audits. Update terminology, constraints, or workflows as the platform evolves.
```

---

## 📋 Quick Reference: Agent Do's & Don'ts

```md
## ✅ DO
- Use the provided `BASE_TEMPLATE` for all page generation
- Include read-only disclaimer in every generated page
- Redact all PHI using `[REDACTED]` or synthetic patterns
- Reference specific regulations (CMS §484, HIPAA 45 CFR)
- Validate links with `mintlify broken-links` before PR
- Queue uncertain content for human review

## ❌ DON'T
- Invent functionality not observed in the UI
- Use real member/employee data in examples
- Document authentication or security internals
- Speculate about unpublished features
- Skip the compliance validation checklist
- Publish without human review for sensitive modules
```

---

## 🔧 Integration Snippets

### Pre-commit Hook for Agent-Generated Files
```bash
# .git/hooks/pre-commit
#!/bin/bash

# Check agent-generated files for compliance markers
for file in $(git diff --cached --name-only | grep "pages/.*\.mdx"); do
if grep -q "generatedBy:" "$file"; then
  # Verify read-only disclaimer
  if ! grep -q "Read-Only Documentation Notice" "$file"; then
    echo "❌ $file missing read-only disclaimer"
    exit 1
  fi
  # Verify no placeholders
  if grep -q "{{" "$file"; then
    echo "❌ $file contains unresolved placeholders"
    exit 1
  fi
fi
done
```

### GitHub Actions Validation Workflow
```yaml
# .github/workflows/agent-docs-validation.yml
name: Validate Agent Documentation
on:
pull_request:
  paths: ['pages/**/*.mdx']

jobs:
validate:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - run: npm install -g mintlify
    - run: mintlify broken-links
    - name: Check agent files
      run: |
        for file in $(git diff --name-only ${{ github.event.pull_request.base.sha }} | grep "pages/.*\.mdx"); do
          if grep -q "generatedBy:" "$file"; then
            echo "Validating agent-generated: $file"
            grep -q "Read-Only Documentation Notice" "$file" || exit 1
            grep -q "{{" "$file" && exit 1
          fi
        done
```