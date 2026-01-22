class Produit:
    material_density_kg_m3 = {
        "Bois": 700,
        "Verre": 2500,
        "Acier": 7700,
        "Aluminium": 2700
    }

    def __init__(self, material, length_mm, width_mm, height_mm):
        self.material = material
        self.length_m = length_mm / 1000
        self.width_m = width_mm / 1000
        self.height_m = height_mm / 1000
        self.volume_m3 = 0
        self.mass_kg = 0
        self.ComputeVolume()
        self.ComputeMass()

    def __str__(self):
        return "[ {} ] length={} width={} height={} {}m3 {}kg".format(
            self.material,
            self.length_m,
            self.width_m,
            self.height_m,
            self.volume_m3,
            self.mass_kg
        )

    def ComputeVolume(self):
        self.volume_m3 = self.length_m * self.width_m * self.height_m
        return self.volume_m3

    def ComputeMass(self):
        self.mass_kg = self.volume_m3 * self.material_density_kg_m3[self.material]
        return self.mass_kg

if __name__ == "__main__":
    p1 = Produit("Bois", 500, 500, 500)
    print(p1)

    p1.length_m = 1
    print(p1)

    p1.ComputeVolume()
    print(p1)

    p1.volume_m3 = p1.ComputeVolume()
    p1.mass_kg = p1.ComputeMass()
    print(p1)