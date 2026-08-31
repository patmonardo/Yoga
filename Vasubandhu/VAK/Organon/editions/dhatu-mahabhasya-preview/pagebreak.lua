local first_unit = true

function Header(header)
  if header.level == 1 and pandoc.utils.stringify(header.content):match("^VAK_1%.") then
    if first_unit then
      first_unit = false
    end
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end
end
