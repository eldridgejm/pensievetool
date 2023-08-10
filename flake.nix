{
  description = "Tool for managing a Pensieve";

  inputs.nixpkgs.url = github:NixOS/nixpkgs/nixos-23.05;

  outputs = {
    self,
    nixpkgs,
  }: let
    supportedSystems = ["x86_64-linux" "x86_64-darwin" "aarch64-darwin"];
    forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);
  in rec {
    pensievetool = forAllSystems (
      system:
        with import nixpkgs {
          system = "${system}";
          allowBroken = true;
        };
          python3Packages.buildPythonPackage rec {
            name = "pensievetool";
            src = ./.;
            propagatedBuildInputs = with python3Packages; [
              markdown
              pygments

              # mdx_linkify
              (
                pkgs.python3Packages.buildPythonPackage rec {
                  pname = "mdx_linkify";
                  version = "2.1";
                  name = "${pname}-${version}";
                  src = builtins.fetchurl {
                    url = "https://files.pythonhosted.org/packages/03/9a/d07599b2e3487d4fa6dca76ecf80ae3d51d135c107d7ead09509a88ecc1d/${name}.tar.gz";
                    sha256 = "sha256:0m4zv1y6cdb243lq2d0qhfb7f4qr6sd0d2r3k0rvcxjh7vj7i4p0";
                  };
                  propagatedBuildInputs = with pkgs.python3Packages; [
                    bleach
                    markdown
                  ];
                }
              )
            ];

            nativeBuildInputs = with python3Packages; [pytest];
            doCheck = false;
          }
    );

    defaultPackage = forAllSystems (
      system:
        pensievetool.${system}
    );
  };
}
