def evaporator(content, evap_per_day, threshold):
    days_counter = 0
    content = 100
    while content >= threshold:
        content *= (1 - evap_per_day / 100)
        days_counter += 1
    return days_counter


if __name__ == '__main__':
    assert evaporator(10, 10, 10) == 22