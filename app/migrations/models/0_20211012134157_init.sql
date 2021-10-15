-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(10) NOT NULL,
    "last_name" VARCHAR(10) NOT NULL,
    "email" VARCHAR(30) NOT NULL
);
COMMENT ON COLUMN "user"."name" IS 'Name user';
COMMENT ON COLUMN "user"."last_name" IS 'Last name user';
COMMENT ON COLUMN "user"."email" IS 'Email user';
CREATE TABLE IF NOT EXISTS "dog" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(10) NOT NULL,
    "picture" VARCHAR(200) NOT NULL,
    "is_adopted" BOOL NOT NULL  DEFAULT True,
    "create_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "idUser_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "dog"."name" IS 'Name dog';
COMMENT ON COLUMN "dog"."picture" IS 'Picture dog';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
