local first_karika = true

function Header(header)
  if header.level == 1 and pandoc.utils.stringify(header.content):match("^VAK_2%.") then
    if first_karika then
      first_karika = false
    end
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end
end
