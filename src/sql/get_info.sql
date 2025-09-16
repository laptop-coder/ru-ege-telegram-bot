SELECT
    (SELECT info FROM orthoepy WHERE used=0 ORDER BY RANDOM() LIMIT 1) AS orthoepy,
    (SELECT info FROM paronyms WHERE used=0 ORDER BY RANDOM() LIMIT 1) AS paronyms,
    (SELECT info FROM phraseological_unit WHERE used=0 ORDER BY RANDOM() LIMIT 1) AS phraseological_unit,
    (SELECT info FROM unstressed_at_root WHERE used=0 ORDER BY RANDOM() LIMIT 1) AS unstressed_at_root;
