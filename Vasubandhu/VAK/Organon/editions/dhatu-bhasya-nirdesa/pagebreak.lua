local first_study = true

function Header(header)
  if header.level == 1 and pandoc.utils.stringify(header.content):match("^VAK_1%.") then
    if first_study then
      first_study = false
    end
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end
end

