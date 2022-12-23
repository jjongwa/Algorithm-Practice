def win(a, b):
    return (4 * a) / (5 * a + 5 * b)


def draw(a, b):
    return (a + b) / (5 * a + 5 * b)


F1, F2, F3, F4 = map(int, input().split())

point_9 = round(win(F1, F2) * win(F1, F3) * win(F1, F4), 5)

point_7 = round(win(F1, F2) * win(F1, F3) * draw(F1, F4), 5) \
          + round(win(F1, F2) * draw(F1, F3) * win(F1, F4), 5) \
          + round(draw(F1, F2) * win(F1, F3) * win(F1, F4), 5)

point_6 = round(win(F1, F2) * win(F1, F3) * win(F4, F1), 5) \
          + round(win(F1, F2) * win(F3, F1) * win(F1, F4), 5) \
          + round(win(F2, F1) * win(F1, F3) * win(F1, F4), 5)

point_5 = round(win(F1, F2) * draw(F1, F3) * draw(F1, F4), 5) \
          + round(draw(F1, F2) * win(F1, F3) * draw(F1, F4), 5) \
          + round(draw(F1, F2) * draw(F1, F3) * win(F1, F4), 5)

point_4 = round(win(F1, F2) * win(F3, F1) * draw(F1, F4) * (1 - win(F3, F2) * win(F4, F2)), 5) \
          + round(win(F1, F2) * win(F4, F1) * draw(F1, F3) * (1 - win(F3, F2) * win(F4, F2)), 5) \
          + round(win(F1, F3) * win(F2, F1) * draw(F1, F4) * (1 - win(F2, F3) * win(F4, F2)), 5) \
          + round(win(F1, F3) * win(F4, F1) * draw(F1, F2) * (1 - win(F2, F3) * win(F4, F2)), 5) \
          + round(win(F1, F4) * win(F3, F1) * draw(F1, F2) * (1 - win(F2, F4) * win(F3, F4)), 5) \
          + round(win(F1, F4) * win(F2, F1) * draw(F1, F3) * (1 - win(F2, F4) * win(F3, F4)), 5)

point_3 = round(win(F1, F2) * win(F3, F1) * win(F4, F1) * win(F3, F2) * win(F3, F4), 5) \
          + round(win(F1, F2) * win(F3, F1) * win(F4, F1) * win(F4, F2) * win(F4, F3), 5) \
          + round(win(F1, F3) * win(F2, F1) * win(F4, F1) * win(F3, F2) * win(F3, F4), 5) \
          + round(win(F1, F3) * win(F2, F1) * win(F4, F1) * win(F2, F3) * win(F2, F4), 5) \
          + round(win(F1, F4) * win(F2, F1) * win(F3, F1) * win(F3, F2) * win(F3, F4), 5) \
          + round(win(F1, F4) * win(F2, F1) * win(F3, F1) * win(F2, F3) * win(F2, F4), 5)

ans = point_3 + point_4 + point_5 + point_6 + point_7 + point_9
print(ans * 100)
