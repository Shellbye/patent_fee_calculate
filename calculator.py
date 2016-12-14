# -*- coding: utf-8 -*-

fee_year = [900, 1200, 2000, 4000, 6000, 8000]


class Patent(object):
    year = 0
    total_fee = 0

    def __repr__(self):
        return "{year}:{fee}".format(year=self.year, fee=self.total_fee)

    def grow(self):
        self.year += 1

    def get_this_year_fee(self):
        if self.year <= 3:
            this_year_fee = fee_year[0]
        elif self.year <= 6:
            this_year_fee = fee_year[1]
        elif self.year <= 9:
            this_year_fee = fee_year[2]
        elif self.year <= 12:
            this_year_fee = fee_year[3]
        elif self.year <= 15:
            this_year_fee = fee_year[4]
        elif self.year <= 20:
            this_year_fee = fee_year[5]
        else:
            this_year_fee = 0
        return this_year_fee

    def get_total_fee(self):
        self.total_fee = 0
        if self.year <= 3:
            self.total_fee = fee_year[0] * self.year
        elif self.year <= 6:
            self.total_fee = fee_year[0] * 3 + fee_year[1] * (self.year - 3)
        elif self.year <= 9:
            self.total_fee = fee_year[0] * 3 + fee_year[1] * 3 + \
                             fee_year[2] * (self.year - 6)
        elif self.year <= 12:
            self.total_fee = fee_year[0] * 3 + fee_year[1] * 3 + \
                             fee_year[2] * 3 + fee_year[3] * (self.year - 9)
        elif self.year <= 15:
            self.total_fee = fee_year[0] * 3 + fee_year[1] * 3 + \
                             fee_year[2] * 3 + fee_year[3] * 3 + \
                             fee_year[4] * (self.year - 12)
        elif self.year <= 20:
            self.total_fee = fee_year[0] * 3 + fee_year[1] * 3 + \
                             fee_year[2] * 3 + fee_year[3] * 3 + \
                             fee_year[4] * 3 + fee_year[5] * (self.year - 15)
        else:
            self.total_fee = 0
        return self.total_fee


def cal(patents_per_year, years):
    index = 0
    patent_list = []
    while index < years:
        index += 1
        patent_list += [Patent() for i in range(patents_per_year)]

        cur_year_fee = 0
        for patent in patent_list:
            patent.grow()
            cur_year_fee += patent.get_this_year_fee()
        print "year No.{index}\tfee:{cur_year_fee}".format(index=index, cur_year_fee=cur_year_fee)

if __name__ == "__main__":
    cal(19, 20)
