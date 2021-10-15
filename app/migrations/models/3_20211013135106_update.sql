-- upgrade --
ALTER TABLE "user" ADD "username" VARCHAR(50);
-- downgrade --
ALTER TABLE "user" DROP COLUMN "username";
