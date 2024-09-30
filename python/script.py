import argparse

def main():
  parser = argparse.ArgumentParser(description="Traitement sur des entiers")
  parser.add_argument("integers", type=int, nargs="+", help="accumulateur d'entiers")
  parser.add_argument("--sum", action="store_true", help="somme les entiers")
  return parser

if __name__ == "__main__":
  parser = main()
  opts = parser.parse_args()
  if opts.sum:
    print(sum(opts.integers))
