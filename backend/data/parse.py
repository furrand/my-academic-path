import json
import sqlite3

# with open("institutions.json") as f:
with open("years.json") as f:
    data = json.load(f)

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

# Prepare insert queries for both tables
# insert_institution_query = """
#     INSERT INTO assist_institution (id, code, begin_id, category, is_community_college, prefers_2016_legacy_report)
#     VALUES (:id, :code, :begin_id, :category, :is_community_college, :prefers_2016_legacy_report)
# """
#
# insert_institutionname_query = """
#     INSERT INTO assist_institutionname (name, institution_id, from_year, alternate_institution_id, has_departments, hide_in_list)
#     VALUES (:name, :institution_id, :from_year, :alternate_institution_id, :has_departments, :hide_in_list)
# """

insert_academicyear_query = """
    INSERT INTO assist_academicyear (id, fall_year)
    VALUES (:id, :fall_year)
"""

# Insert data into assist_institution and assist_institutionnames
with conn:
    for year in data:
        year_data = {"id": year.get("Id"), "fall_year": year.get("FallYear")}
        # for institution in data:
        #     # Set default values for institution fields if missing
        #     institution_data = {
        #         "id": institution.get("id"),
        #         "code": institution.get(
        #             "code", ""
        #         ),  # default to empty string if code is missing
        #         "begin_id": institution.get("beginId", 0),
        #         "category": institution.get("category", 0),
        #         "is_community_college": institution.get("isCommunityCollege", False),
        #         "prefers_2016_legacy_report": institution.get(
        #             "prefers2016LegacyReport", False
        #         ),
        #     }
        #
        # Insert into assist_institution
        # cursor.execute(insert_institution_query, institution_data)
        cursor.execute(insert_academicyear_query, year_data)

        # Insert associated names into assist_institutionnames
        # for name_entry in institution.get("names", []):
        #     # Add a reference to the parent institution's ID
        #     name_entry_data = {
        #         "name": name_entry.get("name", ""),
        #         "institution_id": institution["id"],
        #         "from_year": name_entry.get(
        #             "fromYear"
        #         ),  # This will be None if missing, which inserts as NULL in SQLite
        #         "alternate_institution_id": name_entry.get("alternateInstitutionId"),
        #         "has_departments": name_entry.get("hasDepartments", True),
        #         "hide_in_list": name_entry.get("hideInList", False),
        #     }
        #     cursor.execute(insert_institutionname_query, name_entry_data)

# Close the database connection
conn.close()
