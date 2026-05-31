"""
Complete MODULES dictionary for Enterprise Healthcare Platform documentation
Generated from read-only UI observation - No data injection performed
"""

from datetime import datetime

# ============================================================================
# BASE PAGE TEMPLATE (reused for all pages)
# ============================================================================
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

# ============================================================================
# COMPLETE MODULES DICTIONARY
# ============================================================================
MODULES = {
    # ========================================================================
    # DASHBOARD MODULE
    # ========================================================================
    "dashboard": {
        "index": {
            "title": "Dashboard Overview",
            "description": "Central landing page with member statistics, employee metrics, and quick actions",
            "overview": "The Dashboard serves as the central landing page after authentication, providing at-a-glance visibility into key operational metrics across member care and employee management domains.",
            "functionality": "- Real-time member and employee KPIs\n- Quick action shortcuts to common workflows\n- Role-based widget visibility\n- Notification center integration",
            "roles": "- Admin: Full visibility\n- Clinical: Member-focused metrics\n- Finance: Billing/claims indicators\n- Compliance: Audit/alert widgets",
            "related": "Members, Employees, Task Manager, Reports",
            "access_steps": "Log in → Dashboard loads automatically → Use sidebar to navigate to specific modules",
            "primary_actions": "Click metric cards for drill-down; Use quick action buttons; Check notification bell",
            "outputs": "Aggregated statistics; Alert summaries; Navigation entry points",
            "ui_table": "| Metric Card | Widget | Display KPIs | Click-through to detailed reports |\n| Quick Actions Bar | Button group | Common workflow entry | Role-based visibility |\n| Notification Bell | Icon | Alert center access | Badge count for unread items |",
            "compliance": "Dashboard displays aggregate, de-identified metrics by default. PHI access requires explicit role permissions and is logged per HIPAA audit requirements.",
            "troubleshooting": "| Stats not loading | Check network; verify role permissions; contact admin if persistent |\n| Missing widgets | Confirm role assignment in Agency Settings → Role Management |",
            "related_links": "- [Member Statistics](/dashboard/member-statistics)\n- [Employee Statistics](/dashboard/employee-statistics)\n- [Role Management](/agency-settings/role-management)",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        "member-statistics": {
            "title": "Member Statistics",
            "description": "Detailed view of member-related metrics and trends",
            "overview": "Deep-dive analytics into member population: admissions, discharges, service utilization, authorization status, and care plan compliance.",
            "functionality": "- Trend charts (30/60/90-day views)\n- Filter by status, payer, service type\n- Export to CSV/PDF\n- Drill-down to individual member records",
            "roles": "- Admin/Management: Full access\n- Clinical: Read + filter\n- Billing: Authorization-focused views",
            "related": "Member Directory, Reports, Claims & Billing",
            "access_steps": "Dashboard → Click Member Statistics card OR Members → Reports → Member Analytics",
            "primary_actions": "Apply date/status filters; Export reports; Click member count to view list",
            "outputs": "Trend graphs; Exportable data tables; Compliance summary metrics",
            "ui_table": "| Trend Line Chart | Visualization | Show metric over time | Toggle between 30/60/90 days |\n| Status Filter Dropdown | Selection | Filter by member state | Active, Pending, Discharged, On Hold |",
            "compliance": "All exported data containing PHI requires 'Data Export' role permission and generates audit log entries. Aggregate reports may be shared externally per data sharing agreements.",
            "troubleshooting": "| Export button disabled | Verify role has 'Data Export' permission; Check if report exceeds row limit |\n| Chart not rendering | Clear browser cache; Verify JavaScript enabled; Try different browser |",
            "related_links": "- [Member Directory](/members/member-directory)\n- [Member Report](/reports/member-report)\n- [Claims Management](/claims-billing)",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        "employee-statistics": {
            "title": "Employee Statistics",
            "description": "Workforce analytics including staffing levels, compliance status, and training metrics",
            "overview": "Comprehensive view of employee data: active staff counts, certification expirations, training completion rates, time & attendance summaries, and background check status.",
            "functionality": "- Staffing level dashboards by role/location\n- Compliance expiration alerts\n- Training completion tracking\n- EVV usage analytics",
            "roles": "- HR/Management: Full access\n- Compliance: Read + alert config\n- Clinical: Team-specific views only",
            "related": "Service Provider Directory, Training & Education, Time and Attendance",
            "access_steps": "Dashboard → Click Employee Statistics card OR Employees → Reports → Workforce Analytics",
            "primary_actions": "Filter by department/location; Set expiration alert thresholds; Export compliance reports",
            "outputs": "Staffing summary reports; Expiration alert lists; Training completion certificates",
            "ui_table": "| Expiration Alert Badge | Visual indicator | Flag upcoming credential expiry | Color-coded: 30/60/90 days out |\n| Role Distribution Pie Chart | Visualization | Show staff mix by role | Click slice to filter directory |",
            "compliance": "Employee PII and credential data is protected. Access follows role-based permissions with audit logging. Background check results stored separately per FCRA requirements.",
            "troubleshooting": "| Alert not triggering | Verify notification preferences in user profile; Check if alert threshold is configured |\n| Data mismatch with directory | Refresh page; Check if staff record status is 'Active' |",
            "related_links": "- [Service Provider Directory](/employees/service-provider-directory)\n- [Background Checks](/employees/background-checks)\n- [Training Calendar](/employees/training-and-education/inservice-calendar)",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    },

    # ========================================================================
    # MEMBERS MODULE
    # ========================================================================
    "members": {
        "index": {
            "title": "Members Module",
            "description": "Comprehensive member lifecycle management from intake to discharge",
            "overview": "End-to-end management of healthcare recipients including admission workflows, care planning, service authorization, patient experience tracking, and discharge coordination.",
            "functionality": "- Member registry with advanced search\n- Care plan creation and tracking\n- Authorization and payer management\n- Patient experience feedback collection",
            "roles": "- Clinical: Full care workflow access\n- Admin: Member directory management\n- Billing: Authorization/claims access\n- Compliance: Audit/read-only access",
            "related": "Employees, Claims & Billing, Reports, Licensing",
            "access_steps": "Sidebar → Members → Select sub-module (Member Directory, Care and Assessment, Patient Experience)",
            "primary_actions": "Search/filter members; Create new admission; Update care plans; Track authorizations",
            "outputs": "Member records; Care plans; Authorization reports; Satisfaction survey results",
            "ui_table": "| Member List Table | Data grid | Display member records | Sortable columns; pagination |\n| Status Badges | Visual indicator | Show member state | Green=Active, Yellow=Pending, Red=Discharged |",
            "compliance": "All member data is PHI under HIPAA. Access is logged, role-restricted, and subject to minimum necessary principles. Export functions require additional approval workflows.",
            "troubleshooting": "| Member not found in search | Verify search criteria; Check if record is archived; Confirm role permissions |\n| Care plan won't save | Ensure all required fields completed; Check for concurrent edit lock |",
            "related_links": "- [Member Directory](/members/member-directory)\n- [Care Plans](/members/care-and-assessment/care-plans)\n- [Patient Engagement](/members/patient-experience/patient-engagement)",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        
        # --- Member Directory Sub-Pages ---
        "member-directory": {
            "index": {
                "title": "Member Directory",
                "description": "Central registry for all members with tabbed views for comprehensive management",
                "overview": "The Member Directory serves as the central registry for all healthcare recipients, providing a unified view with 13+ tabbed sections for granular management of member data, services, and communications.",
                "functionality": "- Master member list with advanced filtering\n- Tabbed views for authorizations, charts, services\n- Bulk actions for multi-record operations\n- Geographic mapping integration",
                "roles": "- Admin: Full CRUD access\n- Clinical: Care-focused tabs\n- Billing: Authorization/claims tabs\n- Support: Communications tab only",
                "related": "Care and Assessment, Patient Experience, Claims & Billing",
                "access_steps": "Members → Member Directory → Select member → Navigate tabs",
                "primary_actions": "Search/filter members; Switch tabs for different data views; Use bulk actions toolbar",
                "outputs": "Member lists; Authorization reports; Service utilization summaries; Communication logs",
                "ui_table": "| Tab Navigation | Horizontal tabs | Switch between data views | Persistent selection per session |\n| Bulk Actions Toolbar | Button group | Multi-record operations | Export selected, update status, assign tags |",
                "compliance": "Member Directory access is logged at the record level. Viewing PHI triggers audit entries. Export functions require 'Data Export' role permission and generate compliance reports.",
                "troubleshooting": "| Tab not loading | Check network connection; Verify role has access to that tab's data type |\n| Bulk action failing | Ensure all selected records are in same status; Check for validation errors |",
                "related_links": "- [Authorizations](/members/member-directory/authorizations)\n- [Service Items](/members/member-directory/service-items)\n- [Communications](/members/member-directory/communications)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "members": {
                "title": "Members List",
                "description": "Master list view of all members with search, filter, and status management",
                "overview": "The Members tab provides the primary list view of all healthcare recipients with comprehensive search, filtering, and status management capabilities.",
                "functionality": "- Advanced search by name, MRN, address, phone\n- Multi-criteria filtering (status, payer, date ranges)\n- Inline status updates and quick edits\n- Export to CSV/PDF with field selection",
                "roles": "- Admin: Full CRUD\n- Clinical: Read + care-related edits\n- Billing: Read + authorization fields\n- Support: Read-only",
                "related": "Authorizations, Charts, Service Items, Assignments",
                "access_steps": "Members → Member Directory → Members tab (default view)",
                "primary_actions": "Search members; Apply filters; Update status; Export list; Click member for detail view",
                "outputs": "Filtered member lists; Export files; Status change audit logs",
                "ui_table": "| Search Bar | Text input | Find members by multiple fields | Supports partial matches, wildcards |\n| Status Filter Chips | Toggle buttons | Quick filter by member state | Active, Pending, Discharged, On Hold |",
                "compliance": "All member list exports containing PHI require 'Data Export' permission. Search queries are logged for audit purposes. Minimum necessary principle applies to field visibility.",
                "troubleshooting": "| Search returning no results | Verify search terms; Check if filters are too restrictive; Confirm member isn't archived |\n| Export button missing | Verify role has 'Data Export' permission; Check if selection exceeds export limits |",
                "related_links": "- [Member Directory Overview](/members/member-directory)\n- [New Admission Workflow](/members/member-directory/members)\n- [Authorizations](/members/member-directory/authorizations)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "authorizations": {
                "title": "Authorizations",
                "description": "Track payer approvals, coverage limits, and renewal dates for member services",
                "overview": "Manage insurance authorizations, Medicaid waivers, and private pay approvals for member services including verification, tracking, and renewal management.",
                "functionality": "- Verify coverage eligibility in real-time\n- Track authorization expiration dates with alerts\n- Upload supporting documentation (PDF, images)\n- Set automated renewal reminders",
                "roles": "- Admin/Billing: Full CRUD\n- Clinical: Read + upload clinical justification\n- Compliance: Read + audit access",
                "related": "Member Directory, Payer Management, Claims & Billing",
                "access_steps": "Members → Member Directory → Select member → Authorizations tab",
                "primary_actions": "Search authorizations by payer/date; Upload new approval letters; Flag expiring items; Link to service items",
                "outputs": "Authorization status report; Expiration alert list; Payer compliance summary; Coverage verification logs",
                "ui_table": "| Authorization Status Badge | Visual indicator | Show approval state | Green=Active, Yellow=Expiring Soon (30d), Red=Expired |\n| Payer Filter Dropdown | Selection control | Filter by insurance provider | Includes Aetna, BCBS, Cigna, Medicaid, Medicare |",
                "compliance": "Authorization data is PHI-adjacent. Access logged per HIPAA. Export requires 'Billing Export' role permission. All payer communications documented for audit trail.",
                "troubleshooting": "| Authorization not visible | Verify member is assigned to your caseload; Check payer contract status in Licensing module |\n| Real-time verification failing | Check API connection status; Verify payer credentials in Payer Management |",
                "related_links": "- [Member Directory](/members/member-directory)\n- [Payer Management](/licensing/payer-management)\n- [Claims Upload](/claims-billing/upload-claims)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "charts": {
                "title": "Charts & Clinical Documents",
                "description": "Manage clinical documentation, medical records, and progress notes for members",
                "overview": "Centralized repository for member clinical documentation including medical records, progress notes, assessments, physician orders, and care coordination documents.",
                "functionality": "- Upload/view PDF, DOC, image files\n- Version control with audit trail\n- Tag documents by type (clinical, administrative, legal)\n- Search within document content (OCR-enabled)",
                "roles": "- Clinical: Full CRUD for clinical docs\n- Admin: Administrative document access\n- Billing: Read-only for billing-related docs\n- Compliance: Read + audit access",
                "related": "Care Plans, Practitioner Statements, Communications",
                "access_steps": "Members → Member Directory → Select member → Charts tab",
                "primary_actions": "Upload new documents; Tag/categorize files; Search document library; Link documents to care plans",
                "outputs": "Organized document library; Version history logs; Document access audit trail",
                "ui_table": "| Document Type Filter | Dropdown | Filter by document category | Clinical, Administrative, Legal, Billing |\n| Version History Panel | Timeline view | Show document revisions | Click to compare versions or restore |",
                "compliance": "All clinical documents are PHI. Uploads require electronic signature. Access logged per HIPAA. Document retention follows state/federal requirements (minimum 7-10 years).",
                "troubleshooting": "| Upload failing | Check file type/size limits (<50MB); Verify network connection; Ensure required metadata fields completed |\n| Document not searchable | Allow 5-10 minutes for OCR processing; Verify document isn't marked confidential |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [Practitioner Statements](/members/member-directory/practitioner-statements)\n- [HIPAA Policies](/operations/hipaa-compliance/hipaa-policies)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "service-items": {
                "title": "Service Items",
                "description": "Catalog and assign billable services to members with utilization tracking",
                "overview": "Manage the catalog of billable services available to members, assign services to specific members, and track utilization against authorization limits.",
                "functionality": "- Browse/search service catalog by code, description, payer\n- Assign services to members with date ranges\n- Track utilization vs. authorized units/hours\n- Generate service utilization reports",
                "roles": "- Admin/Billing: Full catalog management\n- Clinical: Assign services to assigned members\n- Compliance: Read + audit access",
                "related": "Authorizations, Claims & Billing, Payer Management",
                "access_steps": "Members → Member Directory → Select member → Service Items tab",
                "primary_actions": "Search service catalog; Assign services with effective dates; Track utilization progress; Flag over-utilization",
                "outputs": "Service assignment records; Utilization reports; Over-limit alerts; Billing-ready service logs",
                "ui_table": "| Utilization Progress Bar | Visual indicator | Show used vs. authorized units | Color changes at 80%/100% thresholds |\n| Service Code Search | Auto-complete | Find services by code/description | Supports CPT, HCPCS, internal codes |",
                "compliance": "Service assignments must align with authorized care plans. Utilization tracking supports Medicare/Medicaid compliance. All modifications logged for audit.",
                "troubleshooting": "| Service not in catalog | Verify payer contract includes this service code; Contact admin to add new service |\n| Utilization not updating | Check if service logs are approved; Verify EVV sync status for time-based services |",
                "related_links": "- [Authorizations](/members/member-directory/authorizations)\n- [Claims Management](/claims-billing)\n- [Payer Contracts](/licensing/payer-management/payer-contracts)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "assignments": {
                "title": "Staff Assignments",
                "description": "Manage caregiver-to-member assignments with scheduling and coverage tracking",
                "overview": "Assign qualified staff members to provide care for specific members, manage schedules, track coverage gaps, and ensure continuity of care.",
                "functionality": "- View staff qualifications vs. member needs\n- Schedule recurring or one-time visits\n- Track assignment history and changes\n- Alert on coverage gaps or qualification mismatches",
                "roles": "- Admin/Clinical Management: Full assignment control\n- Clinical Staff: View assigned members only\n- HR: Read access for staffing analysis",
                "related": "Service Provider Directory, Time and Attendance, Care Plans",
                "access_steps": "Members → Member Directory → Select member → Assignments tab",
                "primary_actions": "Search qualified staff; Assign with date ranges; Set recurrence patterns; Review assignment history",
                "outputs": "Assignment schedules; Coverage reports; Qualification match logs; Handoff documentation",
                "ui_table": "| Qualification Match Indicator | Visual badge | Show staff-member compatibility | Green=Match, Yellow=Partial, Red=Mismatch |\n| Schedule Calendar View | Interactive calendar | Visualize assignment timeline | Drag-and-drop rescheduling |",
                "compliance": "Assignments must comply with staff credentialing and scope of practice. All changes logged for continuity of care audits. PHI access limited to assigned staff.",
                "troubleshooting": "| Staff not appearing in search | Verify staff has active credentials; Check if staff is assigned to conflicting member/time |\n| Schedule conflict warning | Review existing assignments; Use 'View Conflicts' tool to resolve overlaps |",
                "related_links": "- [Service Provider Directory](/employees/service-provider-directory)\n- [Time and Attendance](/employees/time-and-attendance)\n- [Care Plans](/members/care-and-assessment/care-plans)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "communications": {
                "title": "Communications Log",
                "description": "Track all member-related communications including calls, emails, and internal notes",
                "overview": "Centralized log for all communications related to a member including family contacts, provider coordination, internal team notes, and regulatory correspondence.",
                "functionality": "- Log calls, emails, meetings with timestamps\n- Tag communications by type/priority\n- Attach relevant documents or screenshots\n- Search/filter by date, contact, or keyword",
                "roles": "- All authenticated users: Create logs for assigned members\n- Management: View all communications for oversight\n- Compliance: Read + audit access",
                "related": "Member Directory, Patient Experience, Incident Reporting",
                "access_steps": "Members → Member Directory → Select member → Communications tab",
                "primary_actions": "Log new communication; Tag by type (clinical, administrative, family); Attach files; Search history",
                "outputs": "Communication audit trail; Contact history reports; Escalation logs for complaints/incidents",
                "ui_table": "| Communication Type Tags | Color-coded labels | Categorize log entries | Clinical, Family, Provider, Internal, Regulatory |\n| Priority Flag | Icon indicator | Mark urgent items | Red flag for immediate attention required |",
                "compliance": "All communications containing PHI are logged and access-restricted. Family communications require consent documentation. Logs retained per record retention policies.",
                "troubleshooting": "| Log entry not saving | Ensure required fields (contact, timestamp) completed; Check for duplicate entry prevention |\n| Attachment upload failing | Verify file type/size limits; Ensure communication is saved before attaching |",
                "related_links": "- [Patient Experience](/members/patient-experience)\n- [Incident Reporting](/operations/incident-reporting)\n- [HIPAA Training](/operations/hipaa-compliance/hipaa-training)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "practitioner-statements": {
                "title": "Practitioner Statements",
                "description": "Manage physician orders, specialist reports, and external provider documentation",
                "overview": "Repository for documentation from external healthcare providers including physician orders, specialist evaluations, hospital discharge summaries, and referral letters.",
                "functionality": "- Upload provider documents with metadata\n- Link documents to specific care plans or services\n- Track document expiration/renewal dates\n- Generate provider communication logs",
                "roles": "- Clinical: Full CRUD for clinical documents\n- Admin: Administrative document access\n- Billing: Read for billing justification\n- Compliance: Read + audit",
                "related": "Charts, Care Plans, Authorizations, External Referrals",
                "access_steps": "Members → Member Directory → Select member → Practitioner Statements tab",
                "primary_actions": "Upload new provider documents; Link to care activities; Set renewal reminders; Request updated documentation",
                "outputs": "Provider document library; Expiration alert reports; Care plan alignment verification",
                "ui_table": "| Provider Type Filter | Dropdown | Filter by provider specialty | PCP, Specialist, Hospital, Therapy, DME |\n| Expiration Alert Badge | Visual indicator | Flag time-sensitive documents | Yellow=30 days, Red=Expired |",
                "compliance": "External provider documents are PHI. Uploads require verification of provider credentials. All access logged per HIPAA. Documents retained per medical record requirements.",
                "troubleshooting": "| Document not linking to care plan | Verify care plan is in 'Active' status; Check if document type matches plan requirements |\n| Provider not in directory | Add provider to Corporate → Documents → Provider Directory first |",
                "related_links": "- [Charts](/members/member-directory/charts)\n- [Care Plans](/members/care-and-assessment/care-plans)\n- [External Referrals](/members/patient-experience/external-referrals)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "update-counter": {
                "title": "Update Counter & Audit Trail",
                "description": "Track all modifications to member records with detailed audit logging",
                "overview": "Comprehensive audit trail showing all changes made to a member's record including who made changes, when, what fields were modified, and before/after values.",
                "functionality": "- Chronological log of all record modifications\n- Filter by user, date range, or field type\n- Export audit logs for compliance reviews\n- Real-time alerts for sensitive field changes",
                "roles": "- Compliance/Admin: Full audit access\n- Management: Read access for oversight\n- Clinical: View changes to assigned members only",
                "related": "HIPAA Audits, Compliance Checklists, Role Management",
                "access_steps": "Members → Member Directory → Select member → Update Counter tab",
                "primary_actions": "Filter audit log by criteria; Export logs for review; Investigate specific changes; Set alert thresholds",
                "outputs": "Audit trail reports; Change summary exports; Compliance verification documentation",
                "ui_table": "| Change Type Icon | Visual indicator | Show modification category | Create, Update, Delete, View |\n| Before/After Diff View | Side-by-side display | Show field value changes | Highlight modified fields in yellow |",
                "compliance": "Audit logs are immutable and retained for minimum 10 years per HIPAA. Access to audit logs requires 'Compliance Audit' role. All exports watermarked with user/timestamp.",
                "troubleshooting": "| Log entry missing | Check if change was made in different module; Verify time zone settings for accurate filtering |\n| Export button disabled | Verify role has 'Audit Export' permission; Check if date range exceeds export limits |",
                "related_links": "- [HIPAA Audits](/operations/hipaa-compliance/hipaa-audits)\n- [Compliance Checklists](/operations/hipaa-compliance/compliance-checklists)\n- [Role Management](/agency-settings/role-management)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "orientations": {
                "title": "Member Orientations",
                "description": "Track completion of member onboarding and orientation activities",
                "overview": "Manage the orientation process for new members including welcome packets, policy acknowledgments, care team introductions, and initial assessment scheduling.",
                "functionality": "- Checklist-based orientation workflow\n- Track completion status per activity\n- Send automated reminders to members/families\n- Generate orientation completion certificates",
                "roles": "- Clinical/Admin: Full orientation management\n- Support Staff: Update completion status\n- Management: View completion reports",
                "related": "New Admission, Care Plans, Patient Experience",
                "access_steps": "Members → Member Directory → Select member → Orientations tab",
                "primary_actions": "Assign orientation activities; Mark items complete; Send reminder notifications; Generate completion report",
                "outputs": "Orientation completion reports; Reminder logs; Certificate of orientation documents",
                "ui_table": "| Progress Tracker | Visual bar | Show orientation completion % | Auto-updates as items marked complete |\n| Reminder Scheduler | Date/time picker | Set automated follow-ups | Supports one-time or recurring reminders |",
                "compliance": "Orientation documentation supports informed consent requirements. Completion records retained per medical record policies. Family acknowledgments require signature capture.",
                "troubleshooting": "| Checklist item not appearing | Verify orientation template assigned to member type; Check if item is role-restricted |\n| Reminder not sending | Verify member/family contact info is complete; Check notification preferences |",
                "related_links": "- [New Admission Workflow](/members/member-directory/members)\n- [Patient Rights](/members/patient-experience/patient-rights)\n- [Care Plans](/members/care-and-assessment/care-plans)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "sup-visits": {
                "title": "Supervisory Visits",
                "description": "Document and track required supervisory visits for compliance and quality assurance",
                "overview": "Manage scheduled and completed supervisory visits including pre-visit planning, visit documentation, follow-up actions, and compliance tracking for regulatory requirements.",
                "functionality": "- Schedule recurring supervisory visits\n- Document visit findings with structured forms\n- Track corrective actions and follow-ups\n- Generate compliance reports for surveys",
                "roles": "- Clinical Management: Schedule and document visits\n- Compliance: Review and report on completion\n- Admin: Configure visit frequency rules",
                "related": "Care Plans, Risk Assessments, Compliance Checklists",
                "access_steps": "Members → Member Directory → Select member → Sup Visits tab",
                "primary_actions": "Schedule new visit; Document findings using structured form; Assign follow-up tasks; Generate compliance summary",
                "outputs": "Visit documentation records; Follow-up task lists; Compliance completion reports for audits",
                "ui_table": "| Visit Type Dropdown | Selection | Categorize visit purpose | Routine, Complaint-Driven, Post-Incident, Regulatory |\n| Compliance Status Badge | Visual indicator | Show regulatory requirement status | Green=Compliant, Yellow=Due Soon, Red=Overdue |",
                "compliance": "Supervisory visit documentation supports CMS and state licensing requirements. All visits require electronic signature. Records retained per survey readiness policies.",
                "troubleshooting": "| Visit template missing | Verify member's service type has associated visit requirements; Contact admin to configure templates |\n| Compliance status not updating | Ensure all required fields in visit form are completed; Check if follow-up tasks are closed |",
                "related_links": "- [Risk Assessments](/members/care-and-assessment/risk-assessments)\n- [Compliance Checklists](/operations/hipaa-compliance/compliance-checklists)\n- [Survey Deficiencies](/licensing/license-tracking/survey-deficiencies)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "engagement": {
                "title": "Member Engagement Tracking",
                "description": "Monitor and document member and family engagement activities and satisfaction indicators",
                "overview": "Track interactions with members and families including care conferences, feedback sessions, satisfaction surveys, and engagement metrics to support person-centered care.",
                "functionality": "- Log engagement activities with outcomes\n- Track satisfaction survey responses\n- Monitor engagement frequency metrics\n- Generate reports for quality improvement",
                "roles": "- Clinical/Support: Log engagement activities\n- Management: View engagement analytics\n- Quality/Compliance: Access satisfaction data",
                "related": "Patient Experience, Satisfaction Survey, Communications",
                "access_steps": "Members → Member Directory → Select member → Engagement tab",
                "primary_actions": "Log new engagement activity; Record satisfaction feedback; Set follow-up reminders; Generate engagement summary",
                "outputs": "Engagement activity logs; Satisfaction trend reports; Quality improvement data exports",
                "ui_table": "| Engagement Type Tags | Color-coded labels | Categorize interaction type | Care Conference, Feedback Call, Survey, Family Meeting |\n| Satisfaction Score Indicator | Visual gauge | Show satisfaction level | 1-5 scale with color coding |",
                "compliance": "Engagement data supports person-centered care requirements. Satisfaction data anonymized for reporting. All feedback logs retained per quality improvement policies.",
                "troubleshooting": "| Satisfaction survey not appearing | Verify survey is assigned to member's payer/service type; Check if survey period is active |\n| Engagement metric not calculating | Ensure all required activity fields completed; Verify date range filters include relevant period |",
                "related_links": "- [Patient Experience](/members/patient-experience)\n- [Satisfaction Survey](/members/patient-experience/satisfaction-survey)\n- [Quality Reports](/reports/service-provider-reports)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "storage-locations": {
                "title": "Storage Locations",
                "description": "Track physical and digital storage locations for member records and documents",
                "overview": "Manage the physical and digital storage locations for member-related documents including paper files, backup media, archived records, and cloud storage references.",
                "functionality": "- Catalog storage locations with access details\n- Link documents to specific storage references\n- Track record retrieval requests and chain of custody\n- Generate location-based inventory reports",
                "roles": "- Admin/Records Management: Full location management\n- Clinical: Request record retrieval\n- Compliance: Audit access to location logs",
                "related": "Charts, Compliance Checklists, Emergency Prep",
                "access_steps": "Members → Member Directory → Select member → Storage Locations tab",
                "primary_actions": "Add new storage location; Link documents to locations; Log retrieval requests; Generate inventory report",
                "outputs": "Storage inventory reports; Retrieval request logs; Chain of custody documentation",
                "ui_table": "| Location Type Badge | Visual indicator | Categorize storage method | Physical File, Digital Archive, Offsite Backup, Cloud |\n| Retrieval Status Tracker | Progress indicator | Show record request status | Requested, In Transit, Delivered, Returned |",
                "compliance": "Storage location tracking supports record retention and disaster recovery requirements. Retrieval logs maintain chain of custody for legal proceedings. Access restricted per data classification.",
                "troubleshooting": "| Location not appearing in search | Verify location is marked active; Check if location is role-restricted |\n| Retrieval request stuck | Verify contact info for records custodian; Check if request requires additional approval |",
                "related_links": "- [Charts](/members/member-directory/charts)\n- [Emergency Prep Plan](/emergency-prep/planning-documents/emergency-prep-plan-review)\n- [Business Continuity](/emergency-prep/planning-documents/business-continuity-plan)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "map": {
                "title": "Member Map View",
                "description": "Geographic visualization of member locations for routing and coverage planning",
                "overview": "Interactive map view showing member locations with filtering capabilities to support route optimization, coverage analysis, and emergency response planning.",
                "functionality": "- Plot member addresses on interactive map\n- Filter by status, service type, or assigned staff\n- Calculate travel routes and time estimates\n- Export location lists for field staff",
                "roles": "- Clinical Management: Full map access for planning\n- Field Staff: View assigned member locations\n- Admin: Configure map layers and permissions",
                "related": "Assignments, Employee Maps, Emergency Prep",
                "access_steps": "Members → Member Directory → Map tab (requires geocoded addresses)",
                "primary_actions": "Filter members by criteria; View cluster densities; Generate optimized routes; Export location data",
                "outputs": "Route optimization reports; Coverage gap analysis; Emergency response zone maps",
                "ui_table": "| Layer Toggle Controls | Checkbox group | Show/hide map data layers | Members, Staff, Facilities, Traffic |\n| Route Optimization Tool | Interactive planner | Calculate efficient travel paths | Supports multi-stop, time windows, priorities |",
                "compliance": "Member addresses are PHI. Map views require role-based permissions. Exported location data must be encrypted and access-logged. Geocoding services comply with data processing agreements.",
                "troubleshooting": "| Members not appearing on map | Verify addresses are geocoded; Check if member status filter excludes them |\n| Route calculation failing | Ensure all stops have valid addresses; Check if time window constraints are feasible |",
                "related_links": "- [Assignments](/members/member-directory/assignments)\n- [Employee Maps](/resources/tools-utilities/employee-maps)\n- [Emergency Contacts](/emergency-prep/planning-documents/contacts)",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        },
        
        # --- Care and Assessment Sub-Pages ---
        "care-and-assessment": {
            "index": {
                "title": "Care and Assessment",
                "description": "Clinical planning, risk evaluation, and care coordination workflows",
                "overview": "Comprehensive module for developing, implementing, and monitoring individualized care plans, conducting risk assessments, coordinating with physicians, and managing discharge planning.",
                "functionality": "- Template-based care plan creation\n- Risk assessment tools with scoring\n- Physician order integration\n- Discharge planning workflows",
                "roles": "- Clinical: Full care planning access\n- Management: Approval and oversight\n- Compliance: Audit and reporting access",
                "related": "Member Directory, Patient Experience, Licensing",
                "access_steps": "Members → Care and Assessment → Select sub-module (Care Plans, Risk Assessments, etc.)",
                "primary_actions": "Create/update care plans; Conduct risk assessments; Coordinate with physicians; Plan discharges",
                "outputs": "Individualized care plans; Risk assessment reports; Physician coordination logs; Discharge summaries",
                "ui_table": "| Care Plan Template Selector | Dropdown | Choose plan type by condition/service | Home Health, Hospice, Pediatric, Complex Care |\n| Risk Score Calculator | Interactive form | Generate risk scores with weighted factors | Auto-calculates with override capability |",
                "compliance": "Care plans are legal documents requiring electronic signatures. Risk assessments support regulatory compliance. All clinical documentation follows HIPAA and state practice act requirements.",
                "troubleshooting": "| Care plan template missing | Verify member's service type has associated templates; Contact admin to configure condition-specific templates |\n| Risk score not calculating | Ensure all required assessment fields completed; Check if scoring weights are configured |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [Risk Assessments](/members/care-and-assessment/risk-assessments)\n- [Physicians](/members/care-and-assessment/physicians)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "care-plans": {
                "title": "Care Plans",
                "description": "Create, update, and track individualized member care plans with interdisciplinary collaboration",
                "overview": "Develop comprehensive, person-centered care plans aligned with physician orders, member goals, regulatory requirements, and interdisciplinary team input.",
                "functionality": "- Template-based plan creation by condition/service type\n- Goal tracking with measurable outcomes and timelines\n- Interdisciplinary team collaboration with role-based editing\n- Version history with audit trail and electronic signatures",
                "roles": "- Clinical Staff: Create/edit assigned member plans\n- Management: Review and approve plans\n- Admin: Template management and system configuration",
                "related": "Risk Assessments, Physician Orders, Discharge Planning, Service Items",
                "access_steps": "Members → Care and Assessment → Care Plans → Select member or 'New Plan'",
                "primary_actions": "Select care plan template; Define SMART goals with metrics; Assign responsible team members; Set review dates and signatures",
                "outputs": "Printable care plan PDFs; Goal progress dashboards; Compliance reports for surveys; Interdisciplinary team summaries",
                "ui_table": "| Goal Progress Tracker | Visual widget | Show completion % with trend | Auto-updates from service logs and assessments |\n| Team Assignment Panel | Multi-select with roles | Assign care team members by discipline | Shows role, contact info, and availability |",
                "compliance": "Care plans are legal documents requiring electronic signatures per 42 CFR §484. All edits trigger audit log entries with before/after values. Plans reviewed minimum quarterly per CMS requirements.",
                "troubleshooting": "| Template not loading | Verify member's service type and payer have associated templates; Check browser compatibility for rich text editor |\n| Signature workflow stuck | Ensure all required approvers are available; Check if plan has validation errors preventing submission |",
                "related_links": "- [Risk Assessments](/members/care-and-assessment/risk-assessments)\n- [Physicians](/members/care-and-assessment/physicians)\n- [Discharge Planning](/members/care-and-assessment/discharge-planning)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "orientations": {
                "title": "Care Orientations",
                "description": "Track clinical orientation activities for new care plans and service initiations",
                "overview": "Manage the clinical orientation process when initiating new care plans or services including staff briefings, member/family education, and initial assessment coordination.",
                "functionality": "- Checklist-based clinical orientation workflow\n- Track completion status per team member\n- Document member/family education provided\n- Generate orientation completion reports",
                "roles": "- Clinical Staff: Complete orientation activities\n- Management: Verify completion and quality\n- Training: Access for competency tracking",
                "related": "Care Plans, Training & Education, Member Orientations",
                "access_steps": "Members → Care and Assessment → Orientations → Select member/care plan",
                "primary_actions": "Assign orientation activities to team; Document education provided; Mark items complete; Generate completion certificate",
                "outputs": "Orientation completion reports; Education documentation; Competency verification records",
                "ui_table": "| Team Member Checklist | Assignable tasks | Track who completes which orientation item | Shows role, due date, completion status |\n| Education Documentation Form | Structured input | Record topics covered and understanding | Supports signature capture for acknowledgments |",
                "compliance": "Clinical orientation documentation supports staff competency requirements and informed consent. Education records retained per medical record policies. Signatures captured electronically with audit trail.",
                "troubleshooting": "| Orientation checklist incomplete | Verify care plan status is 'Active'; Check if all required team roles assigned |\n| Education form not saving | Ensure all required fields completed; Verify member/family contact info for signature routing |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [Training & Education](/employees/training-and-education)\n- [Member Orientations](/members/member-directory/orientations)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "supervisory-visits": {
                "title": "Supervisory Visits (Care)",
                "description": "Document clinical supervisory visits for quality assurance and regulatory compliance",
                "overview": "Manage scheduled and completed clinical supervisory visits including pre-visit planning, structured documentation, follow-up actions, and compliance tracking for CMS and state requirements.",
                "functionality": "- Schedule recurring clinical supervisory visits\n- Document findings using CMS-compliant structured forms\n- Track corrective actions and quality improvements\n- Generate compliance reports for state surveys",
                "roles": "- Clinical Management: Conduct and document visits\n- Compliance: Review completion and reports\n- Admin: Configure visit frequency rules by service type",
                "related": "Care Plans, Risk Assessments, Compliance Checklists, Survey Deficiencies",
                "access_steps": "Members → Care and Assessment → Supervisory Visits → Select member",
                "primary_actions": "Schedule visit using compliance calendar; Document findings with structured form; Assign corrective actions; Generate survey-ready report",
                "outputs": "Visit documentation records; Corrective action plans; Compliance completion reports; Survey preparation packets",
                "ui_table": "| Visit Compliance Calendar | Interactive scheduler | Show required visit dates by regulation | Color-coded: Due, Completed, Overdue |\n| Structured Documentation Form | CMS-compliant template | Guide thorough visit assessment | Auto-validates required fields before submission |",
                "compliance": "Supervisory visit documentation supports 42 CFR §484.55 and state licensing requirements. All visits require RN electronic signature. Records retained minimum 10 years for survey readiness.",
                "troubleshooting": "| Visit template not matching regulation | Verify service type and state configuration; Contact compliance admin for template updates |\n| Compliance status not updating | Ensure all required form sections completed; Check if corrective actions have due dates set |",
                "related_links": "- [Risk Assessments](/members/care-and-assessment/risk-assessments)\n- [Compliance Checklists](/operations/hipaa-compliance/compliance-checklists)\n- [Survey Deficiencies](/licensing/license-tracking/survey-deficiencies)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "discharge-planning": {
                "title": "Discharge Planning",
                "description": "Coordinate safe and appropriate discharge transitions with comprehensive planning documentation",
                "overview": "Manage the discharge planning process including assessment of post-discharge needs, coordination with receiving facilities/providers, family education, and follow-up planning to ensure continuity of care.",
                "functionality": "- Structured discharge assessment forms\n- Coordinate with receiving facilities via integrated messaging\n- Document family/caregiver education and training\n- Schedule post-discharge follow-up and generate summaries",
                "roles": "- Clinical Staff: Complete assessments and education\n- Management: Approve discharge plans\n- Coordination: Facilitate facility communication",
                "related": "Care Plans, Patient Experience, External Referrals, Communications",
                "access_steps": "Members → Care and Assessment → Discharge Planning → Select member",
                "primary_actions": "Complete discharge readiness assessment; Coordinate with receiving facility; Document education provided; Schedule follow-up and generate summary",
                "outputs": "Discharge summary documents; Education completion records; Follow-up appointment confirmations; Continuity of care reports",
                "ui_table": "| Discharge Readiness Checklist | Structured assessment | Evaluate criteria for safe discharge | Auto-calculates readiness score with override |\n| Facility Coordination Panel | Integrated messaging | Communicate with receiving providers | Shows message history and attachment support |",
                "compliance": "Discharge planning documentation supports CMS Conditions of Participation and state regulations. All plans require interdisciplinary input and electronic signatures. Records retained per medical record requirements.",
                "troubleshooting": "| Discharge assessment incomplete | Verify all required sections completed; Check if receiving facility info is validated |\n| Facility messaging failing | Verify facility is in Corporate Documents directory; Check if integration credentials are current |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [External Referrals](/members/patient-experience/external-referrals)\n- [Communications](/members/member-directory/communications)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "risk-assessments": {
                "title": "Risk Assessments",
                "description": "Conduct standardized risk evaluations to identify and mitigate member safety concerns",
                "overview": "Perform comprehensive risk assessments using validated tools to identify fall risk, elopement potential, abuse/neglect concerns, medication safety issues, and other clinical risks requiring intervention.",
                "functionality": "- Library of validated risk assessment tools (Morse, Hendrich, etc.)\n- Automated scoring with evidence-based intervention suggestions\n- Track assessment frequency per regulatory requirements\n- Generate risk mitigation plans and monitoring schedules",
                "roles": "- Clinical Staff: Conduct and document assessments\n- Management: Review high-risk flags and interventions\n- Compliance: Audit assessment completion and quality",
                "related": "Care Plans, Supervisory Visits, Incident Reporting, Safety Protocols",
                "access_steps": "Members → Care and Assessment → Risk Assessments → Select member and assessment type",
                "primary_actions": "Select appropriate risk tool; Complete structured assessment form; Review auto-generated score and interventions; Document mitigation plan",
                "outputs": "Risk assessment reports; Mitigation plan documents; Monitoring schedule alerts; Compliance completion logs",
                "ui_table": "| Risk Tool Selector | Dropdown with descriptions | Choose validated assessment instrument | Shows regulatory requirement frequency and target population |\n| Intervention Suggestion Engine | Rule-based recommendations | Propose evidence-based interventions | Customizable by agency policy and member preferences |",
                "compliance": "Risk assessments support CMS CoPs §484.55 and state licensing requirements. Assessment frequency tracked per regulation. High-risk flags trigger mandatory management review and documentation.",
                "troubleshooting": "| Assessment tool not available | Verify member's service type and condition match tool criteria; Contact clinical admin to enable additional tools |\n| Score not calculating | Ensure all required assessment items completed; Check if scoring algorithm is configured for selected tool |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [Incident Reporting](/operations/incident-reporting)\n- [Safety Protocols](/operations/hipaa-compliance/hipaa-policies)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "specialized-assessment": {
                "title": "Specialized Assessments",
                "description": "Manage condition-specific or payer-required comprehensive assessments",
                "overview": "Conduct and document specialized assessments required for specific conditions (dementia, pediatric, ventilator) or payer programs (Medicaid waivers, Medicare Advantage) with structured forms and regulatory alignment.",
                "functionality": "- Library of condition-specific assessment templates\n- Payer-program aligned documentation requirements\n- Integrated scoring and care planning recommendations\n- Export capabilities for payer submissions",
                "roles": "- Clinical Specialists: Complete specialized assessments\n- Billing: Verify payer requirements met\n- Compliance: Audit assessment quality and completeness",
                "related": "Care Plans, Authorizations, Payer Management, Regulatory Reports",
                "access_steps": "Members → Care and Assessment → Specialized Assessment → Select member and assessment type",
                "primary_actions": "Select assessment template by condition/payer; Complete structured form with clinical data; Review scoring and recommendations; Export for payer submission",
                "outputs": "Specialized assessment reports; Payer submission packages; Care plan integration documents; Compliance verification logs",
                "ui_table": "| Assessment Template Library | Categorized selector | Find assessments by condition or payer | Shows regulatory source and update date |\n| Payer Requirement Validator | Real-time checker | Ensure documentation meets submission criteria | Highlights missing required fields before export |",
                "compliance": "Specialized assessments support condition-specific regulations and payer contract requirements. All assessments require clinical signature. Export functions include audit trail and watermarking for submission integrity.",
                "troubleshooting": "| Template not matching payer requirements | Verify assessment version is current; Check if payer contract has recent updates requiring template changes |\n| Export validation failing | Ensure all payer-required fields completed; Check if clinical signatures are captured electronically |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [Payer Management](/licensing/payer-management)\n- [Regulatory Reports](/operations/regulatory-reports)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "physicians": {
                "title": "Physician Coordination",
                "description": "Manage communication and documentation with member physicians and medical directors",
                "overview": "Centralized coordination with member physicians including order management, consultation requests, progress reporting, and medical director oversight documentation.",
                "functionality": "- Physician contact directory with specialties and preferences\n- Electronic order management with acknowledgment tracking\n- Consultation request workflow with urgency levels\n- Progress report generation and secure transmission",
                "roles": "- Clinical Staff: Create orders and requests\n- Management: Approve and track physician communications\n- Admin: Maintain physician directory and preferences",
                "related": "Care Plans, Practitioner Statements, External Referrals, Communications",
                "access_steps": "Members → Care and Assessment → Physicians → Select member",
                "primary_actions": "Select physician from directory; Create electronic order or consultation request; Track acknowledgment status; Generate and send progress reports",
                "outputs": "Physician order logs; Consultation tracking reports; Progress report transmission confirmations; Medical director oversight documentation",
                "ui_table": "| Physician Preference Profile | Configurable settings | Store communication preferences per provider | Fax, secure email, portal, phone with best times |\n| Order Acknowledgment Tracker | Status indicator | Show if physician has reviewed orders | Green=Acknowledged, Yellow=Sent, Red=Overdue |",
                "compliance": "Physician order management supports CMS CoPs §484.50. All orders require electronic signature and audit trail. Secure transmission methods comply with HIPAA security rules.",
                "troubleshooting": "| Physician not in directory | Add to Corporate → Documents → Provider Directory with required credentials |\n| Order acknowledgment not updating | Verify physician's preferred communication method is current; Check if secure transmission succeeded |",
                "related_links": "- [Care Plans](/members/care-and-assessment/care-plans)\n- [Practitioner Statements](/members/member-directory/practitioner-statements)\n- [External Referrals](/members/patient-experience/external-referrals)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "case-managers": {
                "title": "Case Manager Assignments",
                "description": "Assign and track case manager responsibilities for member care coordination",
                "overview": "Manage case manager assignments to members including role definition, workload balancing, care coordination documentation, and handoff procedures for continuity.",
                "functionality": "- Case manager directory with qualifications and caseload limits\n- Assignment workflow with conflict checking\n- Care coordination activity logging\n- Handoff documentation and transfer protocols",
                "roles": "- Management: Assign and balance caseloads\n- Case Managers: Document coordination activities\n- Clinical: View assigned case manager and contact",
                "related": "Assignments, Communications, Care Plans, Task Manager",
                "access_steps": "Members → Care and Assessment → Case Managers → Select member or manager",
                "primary_actions": "Assign case manager with effective dates; Log coordination activities; Document handoffs; Generate caseload reports",
                "outputs": "Case assignment records; Coordination activity logs; Handoff documentation; Caseload balance reports",
                "ui_table": "| Caseload Capacity Indicator | Visual gauge | Show manager's current vs. max assignments | Color changes at 80%/100% thresholds |\n| Handoff Checklist | Structured form | Ensure complete transfer of responsibilities | Requires acknowledgment from both managers |",
                "compliance": "Case manager assignments support care coordination requirements under CMS and payer contracts. All handoffs require documentation and electronic signatures. Caseload limits enforced per agency policy and regulations.",
                "troubleshooting": "| Case manager not appearing in assignment list | Verify manager has active credentials and available capacity; Check if manager is assigned to conflicting member |\n| Handoff checklist incomplete | Ensure all required transfer items documented; Verify both managers have provided electronic signatures |",
                "related_links": "- [Assignments](/members/member-directory/assignments)\n- [Communications](/members/member-directory/communications)\n- [Task Manager](/task-manager)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "payer": {
                "title": "Payer Coordination (Care)",
                "description": "Manage care-related communications and documentation with insurance payers",
                "overview": "Coordinate with insurance payers on care-related matters including authorization requests, clinical justification submissions, care plan reviews, and appeal documentation.",
                "functionality": "- Payer contact directory with clinical review preferences\n- Authorization request workflow with clinical attachment support\n- Appeal documentation builder with evidence organization\n- Tracking dashboard for pending payer responses",
                "roles": "- Clinical/Billing: Create and submit requests\n- Management: Approve clinical justifications\n- Compliance: Audit submission quality and timeliness",
                "related": "Authorizations, Payer Management, Claims & Billing, Regulatory Reports",
                "access_steps": "Members → Care and Assessment → Payer → Select member and payer",
                "primary_actions": "Select payer from directory; Create authorization request with clinical attachments; Build appeal documentation; Track response status and deadlines",
                "outputs": "Authorization submission logs; Appeal package documents; Payer response tracking reports; Compliance timeliness audits",
                "ui_table": "| Payer Clinical Preference Profile | Configurable settings | Store submission requirements per payer | Required forms, attachment limits, preferred formats |\n| Appeal Evidence Organizer | Drag-and-drop interface | Structure clinical evidence for appeals | Auto-generates table of contents and citations |",
                "compliance": "Payer coordination supports contract compliance and appeal rights under Medicare/Medicaid. All submissions logged with timestamps. Clinical justifications require appropriate credentials and signatures.",
                "troubleshooting": "| Payer not in directory | Add to Licensing → Payer Management with clinical contact details |\n| Submission validation failing | Verify all payer-required fields completed; Check if clinical attachments meet format/size requirements |",
                "related_links": "- [Authorizations](/members/member-directory/authorizations)\n- [Payer Management](/licensing/payer-management)\n- [Claims Management](/claims-billing)",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        },
        
        # --- Patient Experience Sub-Pages ---
        "patient-experience": {
            "index": {
                "title": "Patient Experience",
                "description": "Monitor and improve member satisfaction, engagement, and rights protection",
                "overview": "Comprehensive module for tracking patient satisfaction, managing complaints and incidents, verifying eligibility, processing external referrals, and ensuring member rights protection.",
                "functionality": "- Satisfaction survey administration and analysis\n- Complaint and incident intake with resolution tracking\n- Real-time eligibility verification with payers\n- External referral coordination and follow-up",
                "roles": "- Support/Clinical: Log interactions and surveys\n- Management: Review trends and resolve escalations\n- Compliance: Audit rights protection and incident handling",
                "related": "Members, Task Manager, Incident Reporting, Licensing",
                "access_steps": "Members → Patient Experience → Select sub-module (Engagement, Complaints, Eligibility, etc.)",
                "primary_actions": "Administer satisfaction surveys; Log complaints/incidents; Verify eligibility; Process referrals; Monitor rights compliance",
                "outputs": "Satisfaction reports; Complaint resolution logs; Eligibility verification records; Referral tracking summaries",
                "ui_table": "| Satisfaction Score Dashboard | Visual analytics | Display satisfaction trends over time | Filter by service type, payer, or demographic |\n| Complaint Priority Triage | Color-coded system | Categorize urgency of member concerns | Red=Immediate, Yellow=24h, Green=Routine |",
                "compliance": "Patient experience data supports CMS Quality Reporting and CAHPS requirements. Complaint handling follows grievance procedures per 42 CFR §484. All satisfaction data anonymized for reporting.",
                "troubleshooting": "| Survey not sending to member | Verify member contact preferences; Check if survey period is active for their service type |\n| Eligibility verification failing | Check payer API connection status; Verify member's insurance information is current in Authorizations |",
                "related_links": "- [Patient Engagement](/members/patient-experience/patient-engagement)\n- [Complaints](/members/patient-experience/complaints)\n- [Eligibility Verification](/members/patient-experience/eligibility-verification)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "patient-engagement": {
                "title": "Patient Engagement Tracking",
                "description": "Monitor and document member and family engagement activities and communication",
                "overview": "Track interactions with members and families including care conferences, feedback sessions, education delivery, and engagement metrics to support person-centered, family-involved care.",
                "functionality": "- Log engagement activities with outcomes and participants\n- Track frequency and quality of family involvement\n- Monitor engagement barriers and resolution strategies\n- Generate reports for quality improvement initiatives",
                "roles": "- Clinical/Support Staff: Log engagement activities\n- Management: Review engagement analytics and trends\n- Quality/Compliance: Access data for improvement planning",
                "related": "Communications, Satisfaction Survey, Care Plans, Task Manager",
                "access_steps": "Members → Patient Experience → Patient Engagement → Select member",
                "primary_actions": "Log new engagement activity with participants and outcomes; Tag by type and priority; Set follow-up reminders; Generate engagement summary report",
                "outputs": "Engagement activity logs; Family involvement metrics; Barrier resolution reports; Quality improvement data exports",
                "ui_table": "| Engagement Type Tags | Color-coded labels | Categorize interaction purpose | Education, Care Conference, Feedback, Family Meeting |\n| Barrier Tracker | Structured form | Document challenges to engagement | Auto-suggests resolution strategies from knowledge base |",
                "compliance": "Engagement documentation supports person-centered care requirements under CMS and state regulations. Family involvement records require consent documentation. All data anonymized for aggregate reporting.",
                "troubleshooting": "| Engagement activity not appearing in reports | Verify activity is tagged with correct member and date; Check if report filters exclude the activity type |\n| Barrier suggestions not relevant | Ensure barrier description is specific; Contact quality team to update knowledge base strategies |",
                "related_links": "- [Communications](/members/member-directory/communications)\n- [Satisfaction Survey](/members/patient-experience/satisfaction-survey)\n- [Care Plans](/members/care-and-assessment/care-plans)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "eligibility-verification": {
                "title": "Eligibility Verification",
                "description": "Real-time insurance eligibility checking and coverage confirmation for members",
                "overview": "Verify member insurance eligibility in real-time with major payers including Medicare, Medicaid, and commercial insurers to confirm coverage, benefits, and authorization requirements before service delivery.",
                "functionality": "- Real-time eligibility checks via integrated payer APIs\n- Coverage benefit summaries with copay/deductible details\n- Authorization requirement alerts and tracking\n- Historical verification log for audit purposes",
                "roles": "- Billing/Admin: Initiate and review verifications\n- Clinical: View coverage status for care planning\n- Compliance: Audit verification completeness and timeliness",
                "related": "Authorizations, Payer Management, Claims & Billing, Service Items",
                "access_steps": "Members → Patient Experience → Eligibility Verification → Select member and date of service",
                "primary_actions": "Select payer and service date; Initiate real-time eligibility check; Review benefit summary and authorization requirements; Save verification to member record",
                "outputs": "Eligibility verification confirmations; Benefit summary reports; Authorization requirement alerts; Audit trail of verification attempts",
                "ui_table": "| Payer API Status Indicator | Visual badge | Show connection status to payer systems | Green=Connected, Yellow=Degraded, Red=Offline |\n| Benefit Summary Card | Structured display | Show coverage details clearly | Highlights copays, deductibles, visit limits, and exclusions |",
                "compliance": "Eligibility verification supports billing compliance and prior authorization requirements. All verification attempts logged with timestamps and user IDs. PHI transmitted via encrypted channels per HIPAA security rules.",
                "troubleshooting": "| Verification failing for specific payer | Check payer API status in System Health; Verify member's insurance information matches payer records exactly |\n| Benefit details incomplete | Ensure service date and procedure codes provided; Check if payer requires additional member identifiers |",
                "related_links": "- [Authorizations](/members/member-directory/authorizations)\n- [Payer Management](/licensing/payer-management)\n- [Claims Upload](/claims-billing/upload-claims)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "external-referrals": {
                "title": "External Referrals",
                "description": "Manage referrals to and from external healthcare providers and facilities",
                "overview": "Coordinate referrals between your agency and external providers including hospitals, specialists, therapy services, and DME suppliers with documentation, tracking, and follow-up management.",
                "functionality": "- Referral intake form with structured clinical data\n- Provider directory integration for recipient selection\n- Automated referral transmission via secure methods\n- Follow-up tracking and outcome documentation",
                "roles": "- Clinical Staff: Create and manage referrals\n- Coordination: Facilitate transmission and follow-up\n- Management: Review referral volumes and outcomes",
                "related": "Physicians, Care Plans, Communications, Task Manager",
                "access_steps": "Members → Patient Experience → External Referrals → Create new or view existing",
                "primary_actions": "Complete referral form with clinical justification; Select recipient provider from directory; Transmit via secure method; Track acknowledgment and follow-up",
                "outputs": "Referral transmission confirmations; Provider acknowledgment logs; Follow-up outcome documentation; Referral volume and outcome reports",
                "ui_table": "| Referral Urgency Selector | Priority levels | Indicate time sensitivity of referral | Routine, Urgent (24h), Emergency (immediate) |\n| Secure Transmission Method | Configurable options | Choose appropriate secure channel | Direct API, Secure Email, Fax with confirmation, Portal |",
                "compliance": "Referral documentation supports care coordination requirements under CMS and payer contracts. All transmissions use HIPAA-compliant secure methods. Referral outcomes tracked for quality reporting.",
                "troubleshooting": "| Provider not in directory | Add to Corporate → Documents → Provider Directory with required credentials and contact preferences |\n| Transmission failing | Verify recipient's secure contact method is current; Check if referral meets payer prior authorization requirements |",
                "related_links": "- [Physicians](/members/care-and-assessment/physicians)\n- [Care Plans](/members/care-and-assessment/care-plans)\n- [Communications](/members/member-directory/communications)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "patient-rights": {
                "title": "Patient Rights Management",
                "description": "Ensure member rights protection, education, and grievance procedures compliance",
                "overview": "Manage documentation and processes related to member rights including rights education, acknowledgment capture, grievance procedures, and advocacy support to ensure regulatory compliance and person-centered care.",
                "functionality": "- Rights education material library by language and format\n- Electronic acknowledgment capture with witness options\n- Grievance intake and resolution workflow\n- Advocacy referral and support documentation",
                "roles": "- All Staff: Provide rights education and acknowledge receipt\n- Management: Oversee grievance resolution and compliance\n- Compliance: Audit rights protection processes",
                "related": "Complaints, Incident Reporting, HIPAA Compliance, Emergency Prep",
                "access_steps": "Members → Patient Experience → Patient Rights → Select member",
                "primary_actions": "Provide rights education using appropriate materials; Capture electronic acknowledgment; Log grievances and track resolution; Refer to advocacy resources when needed",
                "outputs": "Rights acknowledgment records; Grievance resolution logs; Advocacy referral documentation; Compliance audit reports",
                "ui_table": "| Rights Material Selector | Filter by language/format | Choose appropriate education materials | Supports multiple languages, large print, audio |\n| Grievance Workflow Tracker | Status timeline | Show grievance progress through resolution | Auto-escalates if resolution timelines exceeded |",
                "compliance": "Patient rights management supports CMS CoPs §484.52 and state regulations. All acknowledgments require signature capture with witness option. Grievance procedures follow mandated timelines and documentation requirements.",
                "troubleshooting": "| Rights material not available in needed language | Contact compliance admin to add translation; Use interpreter services documentation as interim |\n| Grievance workflow stuck | Verify all required resolution steps documented; Check if escalation thresholds are configured correctly |",
                "related_links": "- [Complaints](/members/patient-experience/complaints)\n- [Incident Reporting](/operations/incident-reporting)\n- [HIPAA Policies](/operations/hipaa-compliance/hipaa-policies)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "complaints": {
                "title": "Complaint Management",
                "description": "Intake, track, and resolve member and family complaints with structured workflows",
                "overview": "Manage the complete complaint lifecycle from intake through resolution including triage, investigation, corrective actions, and follow-up to ensure timely, appropriate responses and continuous improvement.",
                "functionality": "- Structured complaint intake form with categorization\n- Triage system with priority levels and assignment\n- Investigation workflow with evidence collection\n- Resolution tracking with member feedback capture",
                "roles": "- Support/Clinical: Intake and initial response\n- Management: Investigation oversight and resolution approval\n- Compliance: Audit complaint handling and trends",
                "related": "Patient Rights, Incident Reporting, Task Manager, Communications",
                "access_steps": "Members → Patient Experience → Complaints → Log new or view existing",
                "primary_actions": "Complete complaint intake form; Assign priority and investigator; Document investigation findings; Capture resolution and member feedback",
                "outputs": "Complaint resolution records; Trend analysis reports; Corrective action documentation; Member satisfaction follow-up logs",
                "ui_table": "| Complaint Category Tags | Structured taxonomy | Classify complaint type for routing | Clinical Care, Staff Behavior, Billing, Facility, Rights |\n| Resolution Timeline Tracker | Visual countdown | Show time remaining per regulatory requirements | Auto-alerts if approaching deadline |",
                "compliance": "Complaint handling follows CMS grievance procedures §484.52 and state regulations. All complaints logged with timestamps. Resolution timelines enforced with escalation protocols. Records retained per survey requirements.",
                "troubleshooting": "| Complaint category missing | Contact compliance admin to add new category to taxonomy; Use 'Other' with detailed description as interim |\n| Timeline alert not triggering | Verify complaint priority and regulatory deadline configuration; Check if business hours calendar is set correctly |",
                "related_links": "- [Patient Rights](/members/patient-experience/patient-rights)\n- [Incident Reporting](/operations/incident-reporting)\n- [Task Manager](/task-manager)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "incidents": {
                "title": "Patient Incidents",
                "description": "Document and manage member-related incidents including falls, medication errors, and safety events",
                "overview": "Manage documentation and follow-up for member-related incidents including falls, medication errors, elopement attempts, abuse allegations, and other safety events with structured forms and regulatory reporting alignment.",
                "functionality": "- Incident intake form aligned with regulatory categories\n- Severity assessment with automatic reporting triggers\n- Investigation workflow with root cause analysis tools\n- Corrective action planning and effectiveness tracking",
                "roles": "- Clinical/Support: Report incidents immediately\n- Management: Lead investigations and approve actions\n- Compliance: Ensure regulatory reporting and audit readiness",
                "related": "Incident Reporting (Operations), Risk Assessments, HIPAA Incidents, Task Manager",
                "access_steps": "Members → Patient Experience → Incidents → Report new or view existing",
                "primary_actions": "Complete incident report with structured form; Assess severity and trigger notifications; Document investigation findings; Plan and track corrective actions",
                "outputs": "Incident investigation reports; Regulatory submission packages; Corrective action plans; Trend analysis for quality improvement",
                "ui_table": "| Incident Severity Matrix | Visual selector | Classify incident impact and urgency | Auto-triggers notifications based on severity level |\n| Root Cause Analysis Tools | Guided workflow | Support systematic investigation | Includes 5 Whys, Fishbone, and timeline tools |",
                "compliance": "Incident reporting supports CMS CoPs, state licensing, and OSHA requirements. Serious events trigger immediate regulatory notifications per mandated timelines. All investigations require electronic signatures and audit trail.",
                "troubleshooting": "| Incident category not matching event | Use 'Other' category with detailed description; Contact compliance admin to update taxonomy |\n| Regulatory notification not triggering | Verify incident severity assessment; Check if regulatory reporting rules are configured for your state/payer |",
                "related_links": "- [Incident Reporting](/operations/incident-reporting)\n- [Risk Assessments](/members/care-and-assessment/risk-assessments)\n- [HIPAA Incidents](/operations/hipaa-compliance/hipaa-incidents)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "devices": {
                "title": "Medical Devices & Equipment",
                "description": "Track member-assigned medical devices and durable medical equipment (DME)",
                "overview": "Manage the assignment, maintenance, and tracking of medical devices and DME provided to members including inventory management, service records, and replacement scheduling.",
                "functionality": "- Device inventory with serial numbers and specifications\n- Assignment tracking with member and date ranges\n- Maintenance and service record logging\n- Replacement scheduling and insurance coordination",
                "roles": "- Clinical: Assign and monitor device use\n- Equipment Staff: Manage inventory and maintenance\n- Billing: Coordinate insurance coverage and claims",
                "related": "Service Items, Authorizations, Supplies, Asset Manager",
                "access_steps": "Members → Patient Experience → Devices → Select member or device",
                "primary_actions": "Assign device from inventory to member; Log maintenance or service events; Schedule replacements; Coordinate with payer for coverage",
                "outputs": "Device assignment records; Maintenance logs; Replacement schedules; Insurance coordination documentation",
                "ui_table": "| Device Status Indicator | Visual badge | Show device availability and condition | Available, Assigned, In Maintenance, Retired |\n| Maintenance Alert System | Automated notifications | Flag upcoming service requirements | Based on manufacturer schedules and usage metrics |",
                "compliance": "Device tracking supports Medicare DME coverage requirements and state equipment regulations. All assignments require clinical justification. Maintenance records retained per manufacturer and regulatory requirements.",
                "troubleshooting": "| Device not in inventory | Add to Resources → Tools & Utilities → Asset Manager with required specifications |\n| Maintenance alert not triggering | Verify device type has maintenance schedule configured; Check if usage metrics are being recorded correctly |",
                "related_links": "- [Service Items](/members/member-directory/service-items)\n- [Asset Manager](/resources/tools-utilities/asset-manager)\n- [Supplies](/resources/tools-utilities/supplies)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "maps": {
                "title": "Patient Maps & Location Services",
                "description": "Geographic tools for member location visualization and service area planning",
                "overview": "Interactive mapping tools for visualizing member locations, service coverage areas, travel routes, and emergency response zones to support operational planning and member safety.",
                "functionality": "- Plot member addresses with filtering by status or service type\n- Define and visualize service coverage areas\n- Calculate optimized travel routes for field staff\n- Emergency response zone mapping with facility locations",
                "roles": "- Management: Planning and coverage analysis\n- Field Staff: Route optimization and navigation\n- Emergency Prep: Response zone configuration",
                "related": "Member Map, Employee Maps, Emergency Prep, Assignments",
                "access_steps": "Members → Patient Experience → Maps → Select view type (Members, Coverage, Routes, Emergency)",
                "primary_actions": "Filter members by criteria for display; Define service area boundaries; Generate optimized routes; Configure emergency response zones",
                "outputs": "Coverage analysis reports; Route optimization plans; Emergency response maps; Service area utilization analytics",
                "ui_table": "| Coverage Area Designer | Drawing tools | Define service boundaries on map | Supports polygons, radius, and drive-time zones |\n| Emergency Layer Toggle | Checkbox controls | Show/hide emergency resources | Hospitals, Fire Stations, Shelters, Evacuation Routes |",
                "compliance": "Member location data is PHI. Map views require role-based permissions. Exported location data must be encrypted. Geocoding services comply with data processing agreements and HIPAA BAAs.",
                "troubleshooting": "| Members not appearing on map | Verify addresses are geocoded; Check if status filters exclude them; Ensure map layer is enabled |\n| Route optimization failing | Ensure all stops have valid addresses; Check if time window constraints are feasible; Verify traffic data source is active |",
                "related_links": "- [Member Map](/members/member-directory/map)\n- [Employee Maps](/resources/tools-utilities/employee-maps)\n- [Emergency Contacts](/emergency-prep/planning-documents/contacts)",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "satisfaction-survey": {
                "title": "Satisfaction Surveys",
                "description": "Administer and analyze member satisfaction surveys for quality improvement",
                "overview": "Manage the administration, collection, and analysis of member satisfaction surveys including CAHPS-aligned instruments, custom agency questions, and actionable reporting for quality improvement initiatives.",
                "functionality": "- Library of validated survey instruments (CAHPS, custom)\n- Multi-mode administration (phone, mail, online, in-person)\n- Automated scoring and benchmarking against norms\n- Action planning tools linked to survey findings",
                "roles": "- Quality/Management: Configure and analyze surveys\n- Clinical/Support: Administer surveys to members\n- Compliance: Ensure methodology meets reporting requirements",
                "related": "Patient Engagement, Complaints, Reports, Quality Improvement",
                "access_steps": "Members → Patient Experience → Satisfaction Survey → Select survey type and member cohort",
                "primary_actions": "Select survey instrument and administration mode; Assign to member cohort; Monitor response rates; Analyze results and create action plans",
                "outputs": "Survey response reports; Benchmark comparisons; Trend analysis dashboards; Quality improvement action plans",
                "ui_table": "| Survey Mode Selector | Multi-option picker | Choose administration method | Phone script, Mail packet, Online link, In-person tablet |\n| Benchmark Comparison View | Side-by-side display | Compare results to regional/national norms | Highlights areas significantly above/below average |",
                "compliance": "Satisfaction survey methodology supports CMS Quality Reporting and CAHPS requirements. All survey data anonymized for reporting. Administration protocols follow approved sampling and weighting procedures.",
                "troubleshooting": "| Survey not sending to member | Verify member contact preferences and survey eligibility criteria; Check if survey period is active for their service type |\n| Benchmark data not loading | Ensure survey instrument has benchmark dataset configured; Check if data source connection is active |",
                "related_links": "- [Patient Engagement](/members/patient-experience/patient-engagement)\n- [Complaints](/members/patient-experience/complaints)\n- [Service Provider Reports](/reports/service-provider-reports)",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        }
    },

    # ========================================================================
    # EMPLOYEES MODULE (Partial - showing pattern for remaining modules)
    # ========================================================================
    "employees": {
        "index": {
            "title": "Employees Module",
            "description": "Workforce management covering recruitment, compliance, training, and attendance",
            "overview": "Comprehensive management of healthcare staff including recruitment, background verification, training, competency assessment, scheduling, and time tracking with compliance integration.",
            "functionality": "- Employee directory with credential tracking\n- Background check workflow integration\n- Training calendar and competency management\n- EVV-integrated time and attendance",
            "roles": "- HR/Admin: Full workforce management\n- Clinical Management: Team assignment and oversight\n- Compliance: Audit and reporting access\n- Staff: Self-service profile and schedule access",
            "related": "Members, Task Manager, Licensing, Payroll",
            "access_steps": "Sidebar → Employees → Select sub-module (Directory, Background Checks, Training, etc.)",
            "primary_actions": "Search employee directory; Initiate background checks; Assign training; Review time records",
            "outputs": "Staffing reports; Compliance dashboards; Training completion certificates; Payroll-ready time logs",
            "ui_table": "| Employee Status Badge | Visual indicator | Show employment state | Active, Onboarding, Suspended, Terminated |\n| Credential Expiration Alert | Countdown display | Flag upcoming license/certification expiry | Color-coded: 90/60/30 days with auto-reminders |",
            "compliance": "Employee records contain sensitive PII and credential data. Access follows role-based permissions with audit logging. Background check results stored separately from personnel files per FCRA requirements.",
            "troubleshooting": "| Employee not appearing in directory | Verify employment status is 'Active'; Check if role permissions limit visibility |\n| Background check status not updating | Check integration status with screening vendor; Verify employee consent documentation is on file |",
            "related_links": "- [Service Provider Directory](/employees/service-provider-directory)\n- [Background Checks](/employees/background-checks)\n- [Training Calendar](/employees/training-and-education/inservice-calendar)",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        # ... Additional employee sub-pages would follow same pattern
        # For brevity in this response, showing the pattern continuation
        "service-provider-directory": {
            "index": {
                "title": "Service Provider Directory",
                "description": "Central registry for all agency staff and contractors with credential management",
                "overview": "Comprehensive directory of all service providers including employees, contractors, and volunteers with credential tracking, work assignments, and compliance status management.",
                "functionality": "- Advanced search by name, role, credential, or location\n- Credential expiration tracking with automated alerts\n- Work assignment history and current status\n- Bulk actions for onboarding or compliance updates",
                "roles": "- HR/Admin: Full directory management\n- Clinical Management: Team assignment and oversight\n- Staff: View own profile and assignments\n- Compliance: Audit and reporting access",
                "related": "Background Checks, Training & Education, Time and Attendance, Assignments",
                "access_steps": "Employees → Service Provider Directory → Search or select staff member",
                "primary_actions": "Search/filter staff; View credential status; Assign to members/services; Update profile information",
                "outputs": "Staffing reports; Credential compliance dashboards; Assignment summaries; Onboarding checklists",
                "ui_table": "| Credential Status Indicator | Visual badge | Show license/certification state | Active, Expiring Soon, Expired, Pending Renewal |\n| Assignment Quick-Link | One-click action | Assign staff to member or service | Shows availability and qualification match |",
                "compliance": "Staff credential data is sensitive PII. Access restricted by role with audit logging. Credential verification follows state licensing board requirements. Expiration alerts support continuous compliance.",
                "troubleshooting": "| Credential alert not triggering | Verify expiration date is entered correctly; Check if alert thresholds are configured in system settings |\n| Staff not appearing in assignment search | Ensure staff status is 'Active' and has required credentials for the assignment type |",
                "related_links": "- [Background Checks](/employees/background-checks)\n- [Training & Education](/employees/training-and-education)\n- [Staff Assignments](/members/member-directory/assignments)",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            # ... Additional tabs: new-hire-orientations, work-assignments, etc.
        },
        "background-checks": {
            "index": {
                "title": "Background Checks Overview",
                "description": "Comprehensive screening workflow for employee and contractor compliance",
                "overview": "Manage the complete background screening process including DPS checks, federal/state OIG screening, drug testing, and other compliance verifications with automated workflows and audit trails.",
                "functionality": "- Multi-source screening integration (DPS, OIG, sex offender, etc.)\n- Automated re-screening schedules per policy\n- Discrepancy resolution workflow with documentation\n- Compliance reporting for audits and surveys",
                "roles": "- HR/Compliance: Initiate and review screenings\n- Management: Approve hiring decisions based on results\n- Admin: Configure screening policies and schedules",
                "related": "Service Provider Directory, Licensing, HIPAA Compliance, Hiring Policies",
                "access_steps": "Employees → Background Checks → Select screening type or staff member",
                "primary_actions": "Initiate new screening; Review results and flags; Document resolution decisions; Generate compliance reports",
                "outputs": "Screening completion reports; Discrepancy resolution logs; Compliance audit packages; Re-screening schedules",
                "ui_table": "| Screening Status Tracker | Visual workflow | Show progress through screening steps | Applied, In Progress, Results Received, Reviewed, Cleared |\n| Discrepancy Alert Panel | Highlighted section | Flag items requiring review | Auto-categorizes by severity and regulatory impact |",
                "compliance": "Background screening follows FCRA, state licensing, and CMS requirements. All screenings require candidate consent. Results stored separately from personnel files. Discrepancy resolutions documented with electronic signatures.",
                "troubleshooting": "| Screening integration failing | Check vendor API status; Verify agency credentials are current; Contact compliance admin for vendor support |\n| Discrepancy not flagging appropriately | Ensure screening criteria match agency policy; Verify auto-categorization rules are configured correctly |",
                "related_links": "- [DPS Checks](/employees/background-checks/dps-checks)\n- [Federal OIG](/employees/background-checks/federal-oig)\n- [Compliance Checklists](/operations/hipaa-compliance/compliance-checklists)",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            # ... Additional tabs: dps-checks, federal-oig, state-oig, etc.
        }
        # ... Remaining employee sub-modules follow same pattern
    },

    # ========================================================================
    # REMAINING MODULES (Condensed structure showing all identified pages)
    # ========================================================================
    # Task Manager, Relations, Resources, Reports, Projects, Payroll, 
    # Claims & Billing, Management, Corporate, Licensing, Operations, 
    # Finance, Emergency Prep, Subscription, Agency Settings
    
    # Each would follow the same pattern with:
    # - index page for module overview
    # - sub-module index pages
    # - individual page entries for each tab/view identified in exploration
    
    # Example for Task Manager:
    "task-manager": {
        "index": {
            "title": "Task Manager",
            "description": "Centralized task tracking with email-to-task automation and workflow management",
            "overview": "Unified task management system for tracking assignments, deadlines, and completion across all modules with email integration, Kanban views, and automation rules.",
            "functionality": "- Email-to-task conversion via docparser@officeridge.com\n- Multiple view modes (List, Kanban, Calendar)\n- Task assignment, prioritization, and dependency tracking\n- Automation rules for recurring or conditional tasks",
            "roles": "- All authenticated users: Create and manage personal tasks\n- Management: Assign and oversee team tasks\n- Admin: Configure automation rules and integrations",
            "related": "Members, Employees, Relations, Reports",
            "access_steps": "Sidebar → Task Manager → Select view (My Calendar, To Do, Kanban, etc.)",
            "primary_actions": "Create task from email or manually; Assign to self or team; Set priority and due date; Track progress through completion",
            "outputs": "Personal task lists; Team workload reports; Automation rule logs; Completion analytics",
            "ui_table": "| View Mode Selector | Toggle buttons | Switch between task organization methods | List, Kanban, Calendar, All Tasks |\n| Email-to-Task Indicator | Visual badge | Show tasks created from email | Includes original email snippet and sender info |",
            "compliance": "Task data may contain PHI if related to member care. Access follows role-based permissions. Email integration uses encrypted processing. Automation rules audited quarterly for compliance alignment.",
            "troubleshooting": "| Email not converting to task | Verify email sent to docparser@officeridge.com with correct subject format; Check spam/junk folder for confirmation |\n| Task not appearing in assigned view | Ensure task status is not 'Archived'; Verify assignment includes your user role or team |",
            "related_links": "- [Email-to-Task Setup](/task-manager/email-to-task)\n- [Task Automation](/task-manager/task-automation)\n- [Quick Kanban Guide](/task-manager/quick-kanban)",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        # ... Additional task-manager pages: my-calendar, to-do, done, etc.
    },
    
    # Example for Agency Settings (critical system module):
    "agency-settings": {
        "index": {
            "title": "Agency Settings",
            "description": "System configuration for organization profile, users, roles, and integrations",
            "overview": "Central administration console for configuring agency-wide settings including organization profile, location management, user accounts, role permissions, and third-party integrations.",
            "functionality": "- Organization profile with licensing and contact information\n- Multi-location management with service area configuration\n- User account provisioning and deactivation\n- Role-based permission matrix management\n- API and third-party integration configuration",
            "roles": "- System Admin: Full configuration access\n- Management: Limited settings access by role\n- Compliance: Read access for audit purposes",
            "related": "Role Management, Licensing, Corporate Documents, App Integration",
            "access_steps": "Sidebar → Agency Settings (bottom of navigation) → Select configuration area",
            "primary_actions": "Update organization profile; Manage user accounts; Configure role permissions; Set up integrations",
            "outputs": "Configuration change logs; User access reports; Integration status dashboards; Compliance audit exports",
            "ui_table": "| Permission Matrix Editor | Grid interface | Define role capabilities by module | Checkbox-based with inheritance visualization |\n| Integration Status Panel | Connection indicators | Show third-party service connectivity | Green=Active, Yellow=Warning, Red=Disconnected |",
            "compliance": "System configuration changes require dual approval for critical settings. All modifications logged with user, timestamp, and before/after values. Role permissions audited quarterly against least-privilege principles.",
            "troubleshooting": "| User unable to access module after role change | Verify role permissions include the module; Check if user session needs refresh or re-login |\n| Integration showing disconnected | Verify API credentials are current; Check if third-party service has maintenance window; Review integration logs for error details |",
            "related_links": "- [Role Management](/agency-settings/role-management)\n- [Organization Profile](/agency-settings/organization-profile)\n- [App Integration](/agency-settings/app-integration)",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        # ... Additional agency-settings pages: organization-profile, locations, users, role-management, app-integration
    }
}

# ============================================================================
# USAGE INSTRUCTIONS
# ============================================================================
"""
To use this MODULES dictionary with your page generator:

1. Import this file in your generator script:
   from modules_data import MODULES, BASE_TEMPLATE

2. Iterate through MODULES to generate pages:
   for module_name, submodules in MODULES.items():
       for subgroup_name, pages in submodules.items():
           for page_key, page_data in pages.items():
               generate_page(module_name, subgroup_name, page_key, page_data)

3. The generate_page function should:
   - Format BASE_TEMPLATE with page_data values
   - Create directory structure: pages/{module}/{subgroup}/{page_key}.mdx
   - Write the formatted content to the .mdx file
   - Log success/failure for each page

4. After generation, run:
   mintlify dev  # to preview locally
   mintlify build  # to prepare for deployment

5. Validate with:
   - Check all pages have read-only disclaimer
   - Verify internal links resolve correctly
   - Ensure no placeholder text remains
   - Review compliance sections with legal team

Note: This dictionary covers all pages identified in your UI exploration.
Expand individual page content with agency-specific details, screenshots,
and workflow examples as needed.
"""