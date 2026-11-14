def battery_bars(percent):
  lit = percent // 20
  empty = 5 - lit
  return f"[{'#' * lit}{'.' * empty}]"
