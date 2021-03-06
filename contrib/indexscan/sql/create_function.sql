-- select * from readindex('pg_class_oid_index'::regclass) as (ictid tid, hctid tid, aotid text, istatus text, hstatus text, oid oid);

-- We'll be using the function to read indexes on the segments, mark the
-- function as EXECUTE ON ALL SEGMENTS.
CREATE OR REPLACE FUNCTION readindex(oid) RETURNS SETOF record AS
'$libdir/indexscan', 'readindex'
LANGUAGE C STRICT VOLATILE EXECUTE ON ALL SEGMENTS;
