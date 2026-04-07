def trigger_alarm(temperatures, threshold=80):
    alarmed_sensors = []
    for sensor, temp in temperatures.items():
        if temp > threshold:
            alarmed_sensors.append(sensor)
    return alarmed_sensors