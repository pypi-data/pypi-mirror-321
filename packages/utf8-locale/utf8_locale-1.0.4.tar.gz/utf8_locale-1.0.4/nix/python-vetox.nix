# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause

{ pkgs ? import <nixpkgs> { }
, py-ver ? "11"
}:
let
  python-name = "python3${py-ver}";
  python = builtins.getAttr python-name pkgs;
in
pkgs.mkShell {
  buildInputs = [
    pkgs.gitMinimal
    python
  ];
  shellHook = ''
    set -e
    python3.${py-ver} tests/vetox.py run-parallel
    exit
  '';
}
