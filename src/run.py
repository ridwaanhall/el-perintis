from legacy import Legacy
from pewaris import Pewaris
from simulator import Simulator

def main() -> None:
    legacy_pool = [
        Legacy("Platform edukasi syariah", ["Kurang dokumentasi", "Perlu UI modern"]),
        Legacy("Blog trading harian", ["Volatilitas pasar", "Kurang engagement"]),
        Legacy("Framework Django lokal", ["Komunitas kecil", "Kurang maintainer"])
    ]

    pewaris = Pewaris("Ridwan")
    sim = Simulator(pewaris, legacy_pool)
    sim.jalankan()

if __name__ == "__main__":
    main()
