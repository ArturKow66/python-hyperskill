start_h_event = int(input())
start_m_event = int(input())
start_s_event = int(input())
stop_h_event = int(input())
stop_m_event = int(input())
stop_s_event = int(input())

time_passed = ((3600 * stop_h_event + 60 * stop_m_event + stop_s_event) - (3600 * start_h_event + 60 * start_m_event + start_s_event))
print(time_passed)
