import frappe


def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "options": "Rupees",
            "width": 200,
        },
    ]

    data = frappe.db.sql(
        """
        SELECT
            v.make,
            SUM(rb.total_amount) AS total_revenue
        FROM `tabRide Booking` rb
        INNER JOIN `tabVehicle` v
            ON rb.vehicle = v.name
        WHERE rb.docstatus = 1
        GROUP BY v.make
        """,
        as_dict=True,
    )

    chart = {
        "data": {
            "labels": [row.make for row in data],
            "datasets": [
                {
                    "name": "Total Revenue",
                    "values": [row.total_revenue for row in data],
                }
            ],
        },
        "type": "pie",
    }

    return columns, data, "Here is the revenue by make report.", chart