import json

MOD_ROLE=534511381341405184
STREAMER_ROLE=733468896828457001
ROUNDTABLE_ROLE=741356984531550311
LOG_CHANNEL=733415315035390064
MRPS_GUILD=510821302773219331


dyno_data = open("/etc/heroku/dyno").read()
print(dyno_data)
dyno_data = json.loads(dyno_data)
REVISION = dyno_data.get("release").get("commit")[0:7]


