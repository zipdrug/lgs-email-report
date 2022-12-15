CHECK_AUDIT_LEADS_QUERY = '''
SELECT pn.pharmacy_network_type_id AS Network,p."name" AS Pharmacy,p.npi AS NPI,count(DISTINCT(al.patientID)) AS Members,
'' AS Zipcode,1 AS status
FROM audit_lead al INNER JOIN leads l ON al.patientID = l.patient_id 
INNER JOIN pharmacies p ON p.id = l.potential_pharmacy_id AND p.deleted_at IS NULL 
INNER JOIN pharmacies_network pn ON pn.pharmacy_id = p.id AND pn.deleted_at IS NULL 
INNER JOIN pharmacy_network_types pnt ON pnt.id = pn.pharmacy_network_type_id AND pnt.deleted_at IS NULL 
WHERE al.is_success = 'True' AND al.create_dt = '{curr_date}'
AND al.operation ='reassign'
GROUP BY pn.pharmacy_network_type_id,p."name",p.npi 
UNION 
SELECT pn.pharmacy_network_type_id AS Network, '' AS Pharmacy,0 AS NPI,count(DISTINCT(al.patientID)) AS Members, a.postal_code AS Zipcode
,2 AS status
FROM audit_lead al INNER JOIN leads l ON al.patientID = l.patient_id 
INNER JOIN addresses a ON a.patient_id = l.patient_id 
INNER JOIN pharmacies p ON p.id = l.potential_pharmacy_id AND p.deleted_at IS NULL 
INNER JOIN pharmacies_network pn ON pn.pharmacy_id = p.id AND pn.deleted_at IS NULL
INNER JOIN pharmacy_network_types pnt ON pnt.id = pn.pharmacy_network_type_id AND pnt.deleted_at IS NULL 
WHERE al.is_success = 'False' AND al.create_dt = '{curr_date}'
AND al.operation ='reassign'
GROUP BY pn.pharmacy_network_type_id,a.postal_code
'''
