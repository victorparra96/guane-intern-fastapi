-- upgrade --
ALTER TABLE "dog" ALTER COLUMN "picture" DROP NOT NULL;
-- downgrade --
ALTER TABLE "dog" ALTER COLUMN "picture" SET NOT NULL;
