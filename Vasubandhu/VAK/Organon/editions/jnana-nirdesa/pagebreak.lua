function Header(header)
  if header.level == 1 and pandoc.utils.stringify(header.content):match("^VAK_7%.") then
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end
end
