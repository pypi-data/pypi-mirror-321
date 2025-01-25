variable "CASES_TOX3" {
  default = [
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20"},
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py36", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20"},
    {host="py36", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20,<20.27"},
    {host="py36", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20,<20.22"},

    {host="py35", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20"},
    {host="py35", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20,<20.27"},
    {host="py35", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20,<20.22"},

    {host="py27", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20"},
    {host="py27", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20,<20.27"},
    {host="py27", noinstall="py314t py313t py314 py313 py312", notfound="", pass="py311 py310 py39 py38 py37 py36 py35 py27", venv=">=20,<20.22"},
  ]
}

group "test" {
  targets = [
    "tox3",
  ]
}

function "case_name" {
  params = [suite, host_tag, venv_pin]
  result = "test_${suite}_${host_tag}_${regex_replace(venv_pin, "[^0-9]", "_")}"
}

target "__base__" {
  dockerfile = "tests/Dockerfile"
  output = ["type=cacheonly"]
  no-cache = true
}

target "tox3" {
  inherits = ["__base__"]
  target = "tox3"
  name = case_name("tox3", CASE["host"], CASE["venv"])
  matrix = {
    CASE = CASES_TOX3
  }
  args = {
    HOST_TAG = CASE["host"],
    TARGET_TAGS_PASSING = CASE["pass"],
    TARGET_TAGS_NOINSTALL = CASE["noinstall"],
    TARGET_TAGS_NOTFOUND = "${CASE["notfound"]} py20",  # always missing in multipython
    VIRTUALENV_PIN = CASE["venv"],
  }
}

# debug

variable "DEBUG_CASE" {
  default = CASES_TOX3[0]
}

target "debug" {
  inherits = ["__base__"]
  output = ["type=image"]
  target = "debug"
  args = {
    HOST_TAG = DEBUG_CASE["host"],
    TARGET_TAGS_PASSING = DEBUG_CASE["pass"],
    TARGET_TAGS_NOINSTALL = DEBUG_CASE["noinstall"],
    TARGET_TAGS_NOTFOUND = "${DEBUG_CASE["notfound"]} py20",  # always missing in multipython
    VIRTUALENV_PIN = DEBUG_CASE["venv"],
  }
  tags = [
    "tox-multipython-debug",
  ]
}
