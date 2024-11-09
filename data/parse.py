import json
import sqlite3

with open("institutions.json") as f:
    data = json.load(f)

conn = sqlite3.connect("../backend/db.sqlite3")
cursor = conn.cursor()

# Prepare insert queries for both tables
insert_institution_query = """
    INSERT INTO assist_institution (id, code, begin_id, category, is_community_college, prefers_2016_legacy_report)
    VALUES (:id, :code, :beginId, :category, :isCommunityCollege, :prefers2016LegacyReport)
"""

insert_institutionnames_query = """
    INSERT INTO assist_institutionnames (name, institution_id, has_departments, hide_in_list)
    VALUES (:name, :institution_id, :hasDepartments, :hideInList)
"""

# Insert data into assist_institution and assist_institutionnames
with conn:
    for institution in data:
        # Insert into assist_institution
        cursor.execute(insert_institution_query, institution)

        # Insert associated names into assist_institutionnames
        for name_entry in institution["names"]:
            # Add a reference to the parent institution's ID
            name_entry["institution_id"] = institution["id"]
            cursor.execute(insert_institutionnames_query, name_entry)

# Close the database connection
conn.close()
