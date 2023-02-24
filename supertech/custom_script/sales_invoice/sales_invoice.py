import frappe
from frappe.utils import now_datetime, time_diff_in_hours,pretty_date, now, add_to_date
from datetime import datetime

def sendmail1(doc, method):
        notification_email_id = frappe.db.get_value("Email Account", "Notifications", "email_id")
        kiran_email_id = frappe.db.get_value("Email Account", "kiran choudhary gmail", "email_id")
        doc1 = frappe.get_doc("Sales Invoice", doc.name)
        ms = f'''To<br>
{doc1.customer_name}<br><br>
Dear Sir,<br>
Please find below the dispatch particulars against your order no:  {doc1.po_no}
<br><br>
Invoice No: {doc1.name}<br>
Invoice Date: {doc1.posting_date}<br>
Invoice Amount: {doc.grand_total}<br>

Transporter Name: {doc.transporter_name}<br>
L R No: {doc.lr_number} <br>
Freight Basis {doc.local_freight} : 
<br><br>
PFA enclosed LR Copy.
<br><br>
I request you to acknowledge this email as a confirmation when you receive your consignment. 
<br><br>
Once again, thank you for your business. We will look forward for your next order. 
<br><br>
Sincerely, <br>
Supertech Fabrics<br><br>

'''
        
        all_cc = [ kiran_email_id, doc1.i_poc_email, doc1.account_head_email]
        frappe.sendmail(
        recipients =doc1.contact_email,
        subject = "Dispatch details are here",
        message = ms,
        cc = all_cc,
        sender = notification_email_id,
        reference_doctype = "Sales Invoice",
        reference_name	= doc1.name,
        attachments = [{"print_format_attachment": 1, "doctype": "Sales Invoice", "name": doc1.name, "print_format": "Supertech Sales Invoice", "lang": "en-GB"},{"fid": doc1.file},
        
        ]
            
            )
    



