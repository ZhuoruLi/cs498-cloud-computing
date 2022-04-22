CREATE VIEW "powers" ( pk VARCHAR PRIMARY KEY, "personal"."hero"  VARCHAR, "personal"."power"  VARCHAR, "professional"."name"  VARCHAR, "professional"."xp"  VARCHAR, "custom"."color"  VARCHAR);

SELECT p."name" as "Name1", p1."name" as "Name2", p."power" as "Power"
FROM "powers" p JOIN "powers" p1 ON p."power" = p1."power"
WHERE p."hero" = 'yes' and p1."hero" = 'yes';