variable "CASES_TOX4" {
  default = [
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38", noinstall="py37", notfound="py36 py35 py27", venv=">=20"},
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},
  ]
}

variable "CASES_VIRTUALENV" {
  default = [
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", noinstall="", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py36", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20"},
    {host="py36", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.27"},
    {host="py36", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py35", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20"},
    {host="py35", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.27"},
    {host="py35", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},

    {host="py27", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20"},
    {host="py27", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.27"},
    {host="py27", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", noinstall="", notfound="", venv=">=20,<20.22"},
  ]
}

group "test" {
  targets = [
    "tox4",
    "virtualenv",
  ]
}

function "case_name" {
  params = [suite, host_tag, venv_pin]
  result = "test_${suite}_${host_tag}_${regex_replace(venv_pin, "[^0-9]", "_")}"
}

function "case_args" {
  params = [case]
  result = {
    HOST_TAG = case["host"],
    TARGET_TAGS_PASSING = case["pass"],
    TARGET_TAGS_NOINSTALL = case["noinstall"],
    TARGET_TAGS_NOTFOUND = "${case["notfound"]} py20",  # always missing in multipython
    VIRTUALENV_PIN = case["venv"],
  }
}

target "__base__" {
  dockerfile = "tests/Dockerfile"
  output = ["type=cacheonly"]
  no-cache = true
}

target "tox4" {
  inherits = ["__base__"]
  target = "tox4"
  name = case_name("tox4", CASE["host"], CASE["venv"])
  matrix = {
    CASE = CASES_TOX4
  }
  args = case_args(CASE)
}

target "virtualenv" {
  inherits = ["__base__"]
  target = "virtualenv"
  matrix = {
    CASE = CASES_VIRTUALENV
  }
  name = case_name("venv", CASE["host"], CASE["venv"])
  args = case_args(CASE)
  tags = ["virtualenv-multipython-virtualenv"]
}

# debug

target "debug" {
  inherits = ["__base__"]
  output = ["type=image"]
  target = "debug"
  args = case_args(CASES_TOX4[9])  # debug case
  tags = ["virtualenv-multipython-debug"]
}
