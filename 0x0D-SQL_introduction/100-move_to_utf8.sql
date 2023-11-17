-- converts a database to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE second_table
ALTER COLUMN name
TYPE VARCHAR(256) USING name::VARCHAR(256)::UTF8;
