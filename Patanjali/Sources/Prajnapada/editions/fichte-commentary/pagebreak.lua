local first_report = true

function Header(header)
  if header.level == 1 then
    if first_report then
      first_report = false
    end
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end
end
