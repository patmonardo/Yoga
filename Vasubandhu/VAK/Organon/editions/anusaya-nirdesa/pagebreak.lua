function Header(header)
  if header.level == 1 and pandoc.utils.stringify(header.content):match("^VAK_5%.") then
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end
end
