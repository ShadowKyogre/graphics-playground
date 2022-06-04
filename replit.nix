{ pkgs }: {
  deps = [
    pkgs.python38Full
    pkgs.python38Packages.numpy
    pkgs.python38Packages.pyqt5
    pkgs.python38Packages.pygobject3
    pkgs.gobjectIntrospection
    pkgs.gtk3
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Neded for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}
