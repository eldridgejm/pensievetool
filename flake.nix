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
            propagatedBuildInputs = with python3Packages; [markdown pygments];
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
