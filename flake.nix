{
  description = "Python dev flake";

  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable"; };
  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      devShell.x86_64-linux = pkgs.mkShell {
        buildInputs = with pkgs; [
          python311
          python311Packages.pip
          python311Packages.pyls-flake8
          python311Packages.black
          python311Packages.django
          python311Packages.djangorestframework
          python311Packages.graphene-django
          python311Packages.django-cors-headers
        ];
      };
    };
}
