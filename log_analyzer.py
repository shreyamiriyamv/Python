info = 0
warning = 0
error = 0

ip_count = {}
error_types = {}
critical_lines = []

file = open("server_log.txt", "r")

for line in file:

    line = line.strip()
    words = line.split()

    ip = words[0]
    level = words[1]

    if ip in ip_count:
        ip_count[ip] = ip_count[ip] + 1
    else:
        ip_count[ip] = 1

    if level == "INFO":
        info = info + 1

    elif level == "WARNING":
        warning = warning + 1

    elif level == "ERROR":
        error = error + 1

        error_type = " ".join(words[2:])

        if error_type in error_types:
            error_types[error_type] = error_types[error_type] + 1
        else:
            error_types[error_type] = 1

        if "CRITICAL" in line:
            critical_lines.append(line)

file.close()

most_ip = max(ip_count, key=ip_count.get)

print("LOG FILE ANALYZER")
print("---------------------------")

print("INFO messages    :", info)
print("WARNING messages :", warning)
print("ERROR messages   :", error)

print("\nMost Frequent IP Address:")
print(most_ip, "-", ip_count[most_ip], "times")

print("\nErrors by Type:")

for error_type in error_types:
    print(error_type, "-", error_types[error_type])

print("\nCritical Error Lines:")

for line in critical_lines:
    print(line)

result = open("analysis.txt", "w")

result.write("LOG FILE ANALYSIS\n")
result.write("---------------------------\n")
result.write("INFO messages    : " + str(info) + "\n")
result.write("WARNING messages : " + str(warning) + "\n")
result.write("ERROR messages   : " + str(error) + "\n")

result.write("\nMost Frequent IP Address:\n")
result.write(most_ip + " - " + str(ip_count[most_ip]) + " times\n")

result.write("\nErrors by Type:\n")

for error_type in error_types:
    result.write(
        error_type + " - " +
        str(error_types[error_type]) + "\n"
    )

result.write("\nCritical Error Lines:\n")

for line in critical_lines:
    result.write(line + "\n")

result.close()

print("\nResult saved in analysis.txt")
