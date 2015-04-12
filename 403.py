import math
import sys

class Problem():
    def solve(self):
        #self.get(5)
        print([self.get(n) for n in range(1, 100 + 1)])

    def get(self, n):
        total_sum = 0

        for x_1 in range(n + 1):
            lattice_points = self.count_lattice_points(0, x_1)
            total_sum += lattice_points

        for x_1 in range(1, n):
            lattice_points = self.count_lattice_points(1, x_1)
            total_sum += lattice_points

        sqrt_n = int(math.sqrt(n))
        for x_0 in range(2, sqrt_n + 1):
            for x_1 in range(x_0, n // x_0 + 1):
                lattice_points = self.count_lattice_points(x_0, x_1)
                total_sum += lattice_points

        for x_0 in range(1, n + 1):
            for x_1 in range(n // x_0 + 1):
                lattice_points = self.count_lattice_points(-x_0, x_1)
                total_sum += lattice_points

        for x_0 in range(1, sqrt_n + 1):
            for x_1 in range(1, x_0 + 1):
                lattice_points = self.count_lattice_points(-x_0, -x_1)
                total_sum += lattice_points

        for x_0 in range(sqrt_n + 1, n):
            for x_1 in range(1, n // x_0 + 1):
                lattice_points = self.count_lattice_points(-x_0, -x_1)
                total_sum += lattice_points
        #print('total_sum =>', total_sum)
        return total_sum


    def count_under_line(self, x_0_first, x_0_last, x_1_first, x_1_last):
        x_0_sigma_list = self.sigma_list(x_0_first, x_0_last)
        x_1_sigma_list = self.sigma_list(x_1_first, x_1_last)
        double_count = - x_0_sigma_list[3] * x_1_sigma_list[0] \
                + x_0_sigma_list[2] * x_1_sigma_list[1] \
                + x_0_sigma_list[2] * x_1_sigma_list[0] \
                - x_0_sigma_list[1] * x_1_sigma_list[2] \
                - 2 * x_0_sigma_list[1] * x_1_sigma_list[0] \
                + x_0_sigma_list[0] * x_1_sigma_list[3] \
                + x_0_sigma_list[0] * x_1_sigma_list[2] \
                + 2 * x_0_sigma_list[0] * x_1_sigma_list[1] \
                + 2 * x_0_sigma_list[0] * x_1_sigma_list[0]
        return double_count // 2

    def count_under_parabola(self, x_0_first, x_0_last, x_1_first, x_1_last):
        assert(x_0_last <= x_1_first)
        x_0_sigma_list = self.sigma_list(x_0_first, x_0_last)
        x_1_sigma_list = self.sigma_list(x_1_first, x_1_last)
        if x_0_first >= 0:
            six_times_count = 2 * x_0_sigma_list[0] * x_1_sigma_list[3] \
                    + 3 * x_0_sigma_list[0] * x_1_sigma_list[2] \
                    + x_0_sigma_list[0] * x_1_sigma_list[1] \
                    - 2 * x_0_sigma_list[3] * x_1_sigma_list[0] \
                    + 3 * x_0_sigma_list[2] * x_1_sigma_list[0] \
                    - x_0_sigma_list[1] * x_1_sigma_list[0]
            return six_times_count // 6
        elif x_0_last < 0:
            if x_1_first >= 0:
                six_times_count = 2 * x_0_sigma_list[0] * x_1_sigma_list[3] \
                        + 3 * x_0_sigma_list[0] * x_1_sigma_list[2] \
                        + x_0_sigma_list[0] * x_1_sigma_list[1] \
                        - 2 * x_0_sigma_list[3] * x_1_sigma_list[0] \
                        + 3 * x_0_sigma_list[2] * x_1_sigma_list[0] \
                        - x_0_sigma_list[1] * x_1_sigma_list[0]
                return six_times_count // 6
            elif x_1_last < 0:
                six_times_count = 2 * x_0_sigma_list[0] * x_1_sigma_list[3] \
                        + 3 * x_0_sigma_list[0] * x_1_sigma_list[2] \
                        + x_0_sigma_list[0] * x_1_sigma_list[1] \
                        - 2 * x_0_sigma_list[3] * x_1_sigma_list[0] \
                        + 3 * x_0_sigma_list[2] * x_1_sigma_list[0] \
                        - x_0_sigma_list[1] * x_1_sigma_list[0]
                return six_times_count // 6
            else:
                raise NotImplementedError()
        else:
            raise NotImplementedError()


    def count_lattice_points(self, x_0, x_1):
        line = self.count_lattice_points_under_line(x_0, x_1)
        parabola = self.count_lattice_points_under_parabola(x_0, x_1)
        return line - parabola

    def count_lattice_points_under_line(self, x_0, x_1):
        return (x_1 - x_0 + 1) * (x_0**2 + x_1**2 + 2) // 2

    def count_lattice_points_under_parabola(self, x_0, x_1):
        if x_0 >= 0: # 0 <= x_0 <= x_1
            return self.sigma_2(x_1) - self.sigma_2(x_0 - 1)
        elif x_1 >= 0: # x_0 < 0 <= x_1
            return self.sigma_2(x_1) + self.sigma_2(-x_0)
        else: # x_0 <= x_1 < 0 
            return self.sigma_2(-x_0) - self.sigma_2(-x_1 - 1)

    def sigma_list(self, first, last):
        return [
            self.sigma_0(last) - self.sigma_0(first - 1),
            self.sigma_1(last) - self.sigma_1(first - 1),
            self.sigma_2(last) - self.sigma_2(first - 1),
            self.sigma_3(last) - self.sigma_3(first - 1),
        ]

    def sigma_0(self, n):
        return n

    def sigma_1(self, n):
        return n * (n + 1) // 2

    def sigma_2(self, n):
        return n * (n + 1) * (2 * n + 1) // 6

    def sigma_3(self, n):
        return (n * (n + 1) // 2)**2

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
