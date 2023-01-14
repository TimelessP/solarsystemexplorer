import random
from dataclasses import dataclass, field
from datetime import datetime
from typing import Union, List


@dataclass
class Body:
    name: str
    distance_from_sun_km: float
    diameter_at_equator_km: float
    number_of_moons: int
    mass_10e24_kg: float
    surface_gravity_ms2: float
    length_of_day_hours: float
    average_surface_temperature_c: float

    def __hash__(self):
        return hash(self.name)


mercury = Body("Mercury", 57.91e6, 4879, 0, 3.30e23, 3.7, 58.65, 167)
venus = Body("Venus", 108.2e6, 12104, 0, 4.87e24, 8.87, 116.75, 464)
earth = Body("Earth", 149.6e6, 12756, 1, 5.97e24, 9.81, 24, 15)
mars = Body("Mars", 227.9e6, 6792, 2, 6.39e23, 3.71, 24.077, -65)
ceres = Body("Ceres", 413.7e6, 974.3, 0, 9.4e20, 0.27, 9.1, -120)
jupiter = Body("Jupiter", 778.5e6, 142984, 79, 1.90e27, 24.79, 9.92, -110)
saturn = Body("Saturn", 1433.5e6, 120536, 82, 5.68e26, 10.44, 10.656, -140)
uranus = Body("Uranus", 2872.5e6, 51118, 27, 8.68e25, 8.69, 17.24, -195)
neptune = Body("Neptune", 4495.1e6, 49528, 14, 1.02e26, 11.15, 16.11, -200)
pluto = Body("Pluto", 5906.4e6, 2370, 5, 1.31e22, 0.62, 153.3, -225)

bodies = [mercury, venus, earth, mars, ceres, jupiter, saturn, uranus, neptune, pluto]

routes = {
    earth: {mercury, venus, mars},
    mercury: {jupiter},
    venus: {earth},
    mars: {jupiter, saturn, uranus, earth, neptune, ceres},
    ceres: {pluto},
    jupiter: {saturn},
    saturn: {mars},
    uranus: {mars, pluto},
    neptune: {mars},
    pluto: {uranus}
}

# Interesting trivia about the bodies.
radio_chatter_by_body = {
    earth: [
        "Did you know that Earth is the only known planet to have liquid water on its surface?",
        "Did you know that Earth is the third planet from the Sun?",
        "Did you know that Earth is the fifth largest planet in our solar system?",
        "Did you know that Earth is the densest planet in our solar system?",
        "Did you know that Earth has the strongest magnetic field of any planet in our solar system?",
    ],
    mercury: [
        "Did you know that Mercury is the smallest planet in our solar system?",
        "Did you know that Mercury is the closest planet to the Sun?",
        "Did you know that a year on Mercury is only 88 Earth days long?",
        "Did you know that Mercury has a heavily cratered surface?",
        "Did you know that Mercury has a very thin atmosphere that is mostly made up of helium?"
    ],
    venus: [
        "Did you know that Venus is the hottest planet in our solar system?",
        "Did you know that Venus is the brightest object in the night sky after the Moon?",
        "Did you know that Venus has a thick atmosphere that is mostly made up of carbon dioxide?",
        "Did you know that Venus has a day that is longer than its year?",
        "Did you know that Venus has the most volcanoes of any planet in our solar system?"
    ],
    mars: [
        "Did you know that Mars is the fourth planet from the Sun?",
        "Did you know that Mars is also known as the Red Planet?",
        "Did you know that Mars has the largest volcano in the solar system, Olympus Mons?",
        "Did you know that Mars has the longest canyon in the solar system, Valles Marineris?",
        "Did you know that Mars has polar ice caps made of water and carbon dioxide?"
    ],
    ceres: [
        "Did you know that Ceres is the largest object in the asteroid belt between Mars and Jupiter?",
        "Did you know that Ceres was first discovered in 1801 by Italian astronomer Giuseppe Piazzi?",
        "Did you know that Ceres is classified as a dwarf planet by the International Astronomical Union (IAU)?",
        "Did you know that Ceres is the only dwarf planet located in the inner part of our solar system?",
        "Did you know that Ceres has a diameter of about 940 km and its surface is mostly made of water " +
        "ice and clay minerals?"
    ],
    jupiter: [
        "Did you know that Jupiter is the largest planet in our solar system?",
        "Did you know that Jupiter is the fifth planet from the Sun?",
        "Did you know that Jupiter has a Great Red Spot, a giant storm larger than the size of Earth?",
        "Did you know that Jupiter has 79 known moons, the most of any planet in our solar system?",
        "Did you know that Jupiter's atmosphere is mostly made up of hydrogen and helium?"
    ],
    saturn: [
        "Did you know that Saturn is the second largest planet in our solar system?",
        "Did you know that Saturn is the sixth planet from the Sun?",
        "Did you know that Saturn has the most spectacular ring system of any planet in our solar system?",
        "Did you know that Saturn is the least dense planet in our solar system?",
        "Did you know that Saturn has at least 62 known moons, the second most of any planet in our solar system?"
    ],
    uranus: [
        "Did you know that Uranus is the third largest planet in our solar system?",
        "Did you know that Uranus is the seventh planet from the Sun?",
        "Did you know that Uranus is often referred to as an 'ice giant' due to its composition?",
        "Did you know that Uranus has a tilted axis of rotation, which causes extreme seasonal changes?",
        "Did you know that Uranus has 27 known moons, the third most of any planet in our solar system?"
    ],
    neptune: [
        "Did you know that Neptune is the fourth largest planet in our solar system?",
        "Did you know that Neptune is the eighth planet from the Sun?",
        "Did you know that Neptune has the strongest winds of any planet in our solar system, " +
        "reaching speeds of up to 2000 km/h?",
        "Did you know that Neptune has a blue color due to the presence of methane in its atmosphere?",
        "Did you know that Neptune has 14 known moons, the fourth most of any planet in our solar system?"
    ],
    pluto: [
        "Did you know that Pluto was discovered in 1930 by Clyde Tombaugh?",
        "Did you know that Pluto was classified as a planet from its discovery until 2006?",
        "Did you know that Pluto is the largest known dwarf planet in the Solar System?",
        "Did you know that Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra?",
        "Did you know that NASA's New Horizons spacecraft flew by Pluto in 2015, providing the first close-up " +
        "images of the dwarf planet?"
    ]
}


def get_body_by_name(body: str) -> Union[Body, None]:
    for p in bodies:
        if p.name.strip().lower() == body.strip().lower():
            return p

    return None


@dataclass
class Spaceship:
    name: str
    body: Body
    log: List[str] = field(default_factory=list)

    def travel(self, body: Union[Body, str]) -> bool:
        if body in routes[self.body]:
            self.body = body
            return True
        elif get_body_by_name(body) in routes[self.body]:
            self.body = get_body_by_name(body)
            return True

        return False


class Game:
    def __init__(self):
        self.spaceship = Spaceship("Glider 1", random.choice(bodies))

    def play(self):
        print("Welcome to the Solar System Explorer!")
        print("Command your ship to travel to different planets in our solar system to find out interesting things.")
        print("(Enter `help` for a list of commands.)")

        while True:
            print()
            raw_command = input(f"Orbiting {self.spaceship.body.name}> ")
            command = raw_command.strip().lower()

            if "status".startswith(command):
                print(f"You are currently orbiting {self.spaceship.body.name}.")
                print(f"From here, you can travel to: "
                      f"{', '.join([p.name for p in routes[self.spaceship.body]])}")
                continue

            if "radio".startswith(command):
                print(random.choice(radio_chatter_by_body[self.spaceship.body]))
                continue

            if "quit".startswith(command) or "exit".startswith(command):
                print("Thanks for playing!")
                break

            if "travel".startswith(command):
                destination_body = input("Where would you like to travel to? ").strip().lower()
                for body in bodies:
                    if body.name.lower().startswith(destination_body) \
                            and body in routes[self.spaceship.body]:
                        destination_body = body
                        break
                else:
                    print("That is not a valid destination.")
                    continue

                if self.spaceship.travel(destination_body.name):
                    print(f"You are now orbiting {self.spaceship.body.name}.")
                else:
                    print(f"You cannot travel to {destination_body.name} from {self.spaceship.body.name}.")

                continue

            if "database".startswith(command):
                print(f"Database information relating to {self.spaceship.body.name}:")
                print(f"\tDistance from the sun (km): {self.spaceship.body.distance_from_sun_km:.2e}")
                print(f"\tDistance from the sun (au): "
                      f"{self.spaceship.body.distance_from_sun_km / 149597870.7:0.2f}")
                print(f"\tDiameter (km): {self.spaceship.body.diameter_at_equator_km:,}")
                print(f"\tMass (kg): {self.spaceship.body.mass_10e24_kg:.2e}")
                print(f"\tSurface gravity (m/s^2): {self.spaceship.body.surface_gravity_ms2}")
                print(f"\tNumber of moons: {self.spaceship.body.number_of_moons}")
                print(f"\tLength of day (hours): {self.spaceship.body.length_of_day_hours}")
                print(f"\tAverage surface temperature (C): {self.spaceship.body.average_surface_temperature_c}")

                continue

            if "log".startswith(command):
                print("Ship's Log:")
                if not self.spaceship.log:
                    print("\tNo entries.")
                else:
                    for entry in self.spaceship.log:
                        print(f"\t{entry}")

                continue

            if "log".startswith(command.split()[0]):
                log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - " \
                            f"{self.spaceship.body.name} - " \
                            f"{' '.join(raw_command.strip().split()[1:])}"
                self.spaceship.log.append(log_entry)
                print("Entry added to ship's log.")
                continue

            if "routes".startswith(command):
                print("Routes:")
                for body in bodies:
                    for route in routes[body]:
                        print(f"\t{body.name} --> {route.name}")

                continue

            if "help".startswith(command):
                print("Available commands: status, database, radio, travel, log, routes, quit")
                continue

            print("That is not a valid command.")


if __name__ == '__main__':
    game = Game()
    game.play()
