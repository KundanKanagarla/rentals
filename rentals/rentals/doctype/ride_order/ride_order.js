// Copyright (c) 2026, KK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {
        comsole.log("running load...");
    },
    setup(frm){
        console.log("setup...");
    },
	refresh(frm) {
        console.log("on refresh...");

        if(frm.doc.status === "New"){
            frm.add_custom_button("Accept",() => {
                // status => approved
                frm.set_value("status","Accepted");
                // save the form
                frm.save();
            },"Actions")
            frm.add_custom_button("Reject",() => {
                // status => approved
                frm.set_value("status","Rejected");
                // save the form
                frm.save();
            },"Actions")
        }
        
	},
    status(frm){
        console.log("status changed...");
    }
});
