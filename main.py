from log_system import LogSystem


if __name__ == "__main__":
    obj = LogSystem()
    obj.put(0, "2017:01:01:23:59:59")
    param_2 = obj.retrieve(
        start="2017:01:01:23:59:59", end="2017:01:02:23:59:59", granularity="Day"
    )
