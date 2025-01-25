# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause

{ pkgs ? import <nixpkgs> { }
, py-ver ? "11"
}:
let
  python-name = "python3${py-ver}";
  python = builtins.getAttr python-name pkgs;
  python-pkgs = python.withPackages (p: with p; [
    pyparsing
    pytest
  ]);
in
pkgs.mkShell {
  buildInputs = [ python-pkgs ];
  shellHook = ''
    set -e
    PYTHONPATH="$(pwd)/python" python3.${py-ver} -m pytest -v python/unit_tests
    exit
  '';
}
