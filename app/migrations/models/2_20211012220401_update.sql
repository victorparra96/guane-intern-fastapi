-- upgrade --
ALTER TABLE "user" ADD "hashed_password" VARCHAR(200);
-- downgrade --
ALTER TABLE "user" DROP COLUMN "hashed_password";
