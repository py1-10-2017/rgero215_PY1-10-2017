-- 1
SELECT SUM(billing.amount) AS total_revenue
FROM billing
WHERE MONTH(billing.charged_datetime) = 3 AND YEAR(billing.charged_datetime) = 2012;

-- 2
SELECT SUM(billing.amount) AS total_revenue
FROM billing
JOIN clients ON billing.client_id = clients.client_id
WHERE clients.client_id = 2;

-- 3
SELECT  sites.domain_name
FROM sites
JOIN clients ON clients.client_id = sites.client_id
WHERE sites.client_id = 10;

-- 4
SELECT clients.client_id, COUNT(sites.domain_name) AS total, MONTH(sites.created_datetime) AS per_month, YEAR(sites.created_datetime) AS per_year
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 1
GROUP BY per_month, per_year;

SELECT clients.client_id, COUNT(sites.domain_name) AS total, MONTH(sites.created_datetime) AS per_month, YEAR(sites.created_datetime) AS per_year
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 20
GROUP BY per_month, per_year;

-- 5

SELECT COUNT(leads.leads_id) AS total_leads, sites.domain_name
FROM sites
JOIN  leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.domain_name;

-- 6

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, COUNT(leads.leads_id) AS total_leads, sites.domain_name
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY leads.registered_datetime;

-- 7

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, MONTHNAME(leads.registered_datetime) as month_2011, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY name, month_2011
ORDER BY MONTH(leads.registered_datetime);

-- 8

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, MONTHNAME(leads.registered_datetime) as month_2011, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY name, month_2011
ORDER BY clients.client_id;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, sites.domain_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
GROUP BY name, sites.domain_name
ORDER BY clients.client_id;

-- 9

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, MONTHNAME(billing.charged_datetime) AS bill_month, YEAR(billing.charged_datetime) AS bill_year, billing.amount
FROM clients
JOIN billing ON billing.client_id = clients.client_id
GROUP BY name, bill_month, bill_year
ORDER BY clients.client_id;

-- 10

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, GROUP_CONCAT(' ', sites.domain_name) AS sites
FROM clients
JOIN sites ON sites.client_id = clients.client_id
GROUP BY name
ORDER BY clients.client_id;
