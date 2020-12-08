

class User():

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def __setattr__(self, name, value):
        if name == 'rank' and value == 8:
            self.progress = 0
        super().__setattr__(name,value)


    def inc_progress(self,rank):
        if rank not in range(-8,9) or rank == 0:
            raise ValueError("Questions can only be within the range of -8 to 8.")
        q_rank = rank
        user_rank = self.rank

        diff = q_rank - user_rank
        # Ignoring zero in rank difference
        if (q_rank < 0 and user_rank < 0) or (q_rank > 0 and user_rank > 0):
            pass
        elif diff > 0:
            diff -=1
        elif diff < 0:
            diff += 1


        if diff <= -2:
            prog = 0
        elif diff == -1:
            prog = 1
        elif diff == 0:
            prog = 3
        elif diff > 0:
            prog = 10 * diff * diff

        self.progress += prog

        while self.progress >= 100:

            if self.rank != -1:
                self.rank += 1
            else:
                self.rank += 2
            self.progress -= 100

        if self.rank >= 8:
            self.rank = 8
            self.progress = 0




user = User()

for num in [8 ,-1 ,-7 ,-4 ,7 ,4 ,-3 ,-4 ,8 ,8]:
    print(user.rank, user.progress)
    user.inc_progress(num)



