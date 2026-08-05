class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = sorted(zip(position, speed), reverse = True)

        limittime = 0.0
        fleet = 0

        for p, s in zipped:
            time = (target - p) / s
            if time > limittime:
                fleet += 1
                limittime = time
        return fleet
            