import frappe
from frappe.utils import now_datetime, time_diff_in_hours,pretty_date, now, add_to_date
from datetime import datetime
from email.utils import formataddr

def sendmail1(doc, method):
        supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
        sender_name = "Supertech"
        director = frappe.db.get_value("Email Account", "choudharykiran9721@gmail.com", "email_id")
        # plant_manager = "gaurang@supertechfabrics.com"
        plant_manager = "mrinal.a@indictranstech.com "
        ms = f'''To<br>
{doc.customer_name}<br><br>
Dear Sir,<br>
Please find below the dispatch particulars against your order no:  {doc.po_no}
<br><br>
Invoice No : {doc.name}<br>
Invoice Date : { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
Invoice Amount : {doc.get_formatted("grand_total") }<br>

Transporter Name : {doc.transporter_name}<br>
L R No : {doc.lr_number} <br>
Freight Basis : {doc.local_freight} 
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
        
        all_cc = [ director, plant_manager, doc.i_poc_email, doc.account_head_email]
        sender = formataddr((sender_name, supertech))
        frappe.sendmail(
        recipients =doc.contact_email,
        subject = "Dispatch details are here",
        message = ms,
        cc = all_cc,
        sender = sender,
        reference_doctype = "Sales Invoice",
        reference_name	= doc.name,
        now =  True,
        expose_recipients = "header",
        read_receipt = 0,
        is_notification = False,
        attachments = [{"print_format_attachment": 1, "doctype": "Sales Invoice", "name": doc.name, "print_format": "Supertech Sales Invoice", "lang": "en-GB"},{"fid": doc.file},
        
        ]
            
            )

