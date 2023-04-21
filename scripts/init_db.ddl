CREATE EXTENSION "uuid-ossp";

DROP TABLE IF EXISTS educational_modules;

CREATE TABLE educational_modules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    module_number INT NOT NULL,
    module_name TEXT NOT NULL,
    module_description TEXT NOT NULL
);