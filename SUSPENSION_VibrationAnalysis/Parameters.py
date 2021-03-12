class Car:
    def __init__(self, driver_mass=70.0, car_mass=180.0, total_mass=250.0,
                 perc_sprung_mass=0.8, sprung_mass=150, unsprung_mass=100,
                 front_right_unsprung_mass=20, front_left_unsprung_mass=20,
                 rear_right_unsprung_mass=30, rear_left_unsprung_mass=30,
                 wheelbase=1.6, perc_weight_front=0.6, front_wb2CG=0.9, rear_wb2CG=0.7,
                 track=1.4, perc_weight_right=0.5,right_wb2CG=0.7, left_wb2CG=0.7):
        """
        BASIC CAR PARAMETERS
        :param driver_mass: driver mass [kg]
        :param car_mass: car mass [kg]
        :param total_mass: driver + car masses [kg]
        :param perc_sprung_mass: percentage of car sprung mass []
        :param sprung_mass: car sprung mass [kg]
        :param unsprung_mass: car unsprung mass [kg]
        :param front_right_unsprung_mass: front right side unsprung mass [kg]
        :param front_left_unsprung_mass: front left side unsprung mass [kg]
        :param rear_right_unsprung_mass: rear right side unsprung mass [kg]
        :param rear_left_unsprung_mass: rear left side unsprung mass [kg]
        :param wheelbase: distance between the front and the rear wheel center [m]
        :param perc_weight_front: percentage of weight on the car front axle []
        :param front_wb2CG: distance between the front wheel center and the car CG [m]
        :param rear_wb2CG: distance between the rear wheel center and the car CG [m]
        :param track: distance between the right and the left wheel center [m]
        :param perc_weight_right: percentage of weight on the car right side []
        :param right_wb2CG: distance between the right wheel center and the car CG [m]
        :param left_wb2CG: distance between the left wheel center and the car CG [m]
        """
        self.driver_mass=driver_mass
        self.car_mass=car_mass
        self.total_mass=total_mass
        self.perc_sprung_mass=perc_sprung_mass
        self.sprung_mass=sprung_mass
        self.unsprung_mass=unsprung_mass
        self.front_right_unsprung_mass=front_right_unsprung_mass
        self.front_left_unsprung_mass = front_left_unsprung_mass
        self.rear_right_unsprung_mass = rear_right_unsprung_mass
        self.rear_left_unsprung_mass = rear_left_unsprung_mass
        self.wheelbase=wheelbase
        self.perc_weight_front=perc_weight_front
        self.front_wb2CG=front_wb2CG
        self.rear_wb2CG = rear_wb2CG
        self.track = track
        self.perc_weight_right=perc_weight_right
        self.right_wb2CG = right_wb2CG
        self.left_wb2CG = left_wb2CG

    def update_weights(self):
        self.sprung_mass = self.perc_sprung_mass * self.total_mass
        self.unsprung_mass = self.total_mass - self.sprung_mass




class Suspension:
    def __init__(self, K):
        self.K=K