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
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py314t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py313t", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py314", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py313", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py312", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py311", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py310", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py39", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py38", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20"},  # be ready to fail "py37"
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37", notfound="py36 py35 py27", venv=">=20,<20.27"},
    {host="py37", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py36", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py36", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py36", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py35", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py35", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py35", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},

    {host="py27", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20"},
    {host="py27", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.27"},
    {host="py27", pass="py314t py313t py314 py313 py312 py311 py310 py39 py38 py37 py36 py35 py27", notfound="", venv=">=20,<20.22"},
  ]
}

group "test" {
  targets = [
    "tox4",
    "virtualenv",
  ]
}

target "__base__" {
  dockerfile = "tests/Dockerfile"
  output = ["type=cacheonly"]
  no-cache = true
}

target "tox4" {
  inherits = ["__base__"]
  target = "tox4"
  name = "test_tox4_${CASE["host"]}_${regex_replace(CASE["venv"], "[^0-9]", "_")}"
  matrix = {
    CASE = CASES_TOX4
  }
  args = {
    HOST_TAG = CASE["host"],
    TARGET_TAGS_PASSING = CASE["pass"],
    TARGET_TAGS_NOINSTALL = CASE["noinstall"],
    TARGET_TAGS_NOTFOUND = "${CASE["notfound"]} py20",  # always missing in multipython
    VIRTUALENV_PIN = CASE["venv"],
  }
}

target "virtualenv" {
  inherits = ["__base__"]
  target = "virtualenv"
  name = "test_venv_${CASE["host"]}_${regex_replace(CASE["venv"], "[^0-9]", "_")}"
  matrix = {
    CASE = CASES_VIRTUALENV
  }
  args = {
    HOST_TAG = CASE["host"],
    TARGET_TAGS_PASSING = CASE["pass"],
    TARGET_TAGS_NOINSTALL = "",
    TARGET_TAGS_NOTFOUND = "${CASE["notfound"]} py20",  # always missing in multipython
    VIRTUALENV_PIN = CASE["venv"],
  }
}

# debug

target "debug" {
  inherits = ["__base__"]
  output = ["type=image"]
  target = "debug"
  args = {
    MULTIPYTHON_DEBUG = "true",
    HOST_TAG = "py313",
    TARGET_TAGS_PASSING = "py314t py313t py314 py313 py312 py311 py310 py39 py38",
    TARGET_TAGS_NOINSTALL = "py37",
    TARGET_TAGS_NOTFOUND = "py36 py35 py27 py20",
    VIRTUALENV_PIN = ">=20",
  }
  tags = [
    "virtualenv-multipython-debug",
  ]
}
