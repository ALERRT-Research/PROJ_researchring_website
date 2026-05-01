# _render_media.R
# ─────────────────────────────────────────────────────────────────
# Shared helpers for rendering media/news entries from _media_entries.yaml.
# Sourced by index.qmd (news strip) and public_media.qmd (full media page).
#
# HOW TO ADD NEW ENTRIES:
#   Edit _media_entries.yaml — add a block at the TOP of that file.
#   Both pages regenerate automatically on the next `quarto render`.
#   No other files need touching.
# ─────────────────────────────────────────────────────────────────

library(yaml)

read_media_entries <- function(path = "_media_entries.yaml") {
  entries <- yaml::read_yaml(path)
  entries[order(sapply(entries, function(x) as.Date(x$date)), decreasing = TRUE)]
}

# ── Landing page news strip ───────────────────────────────────────

render_news_strip_html <- function(entries, n = 5) {
  top <- head(entries, n)
  items <- sapply(top, function(e) {
    display_title <- if (!is.null(e$landing_title)) e$landing_title else e$title
    date_fmt <- trimws(format(as.Date(e$date), "%B %e, %Y"))
    sprintf(
      '<div class="rr-media-item">\n  <div class="rr-media-meta">%s</div>\n  <a class="rr-media-title" href="%s" target="_blank">%s</a>\n</div>',
      date_fmt, e$url, display_title
    )
  })
  cat(paste(c(
    '<section class="rr-media-strip">',
    '  <div class="rr-media-strip-label">News &amp; Updates</div>',
    items,
    '  <a class="rr-media-see-all" href="public_media.html">View all media &rarr;</a>',
    '</section>'
  ), collapse = "\n"))
}

# ── Full media page renderers ─────────────────────────────────────

render_news_html <- function(e) {
  date_fmt <- format(as.Date(e$date), "%B %d, %Y")
  desc_html <- if (!is.null(e$description)) {
    sprintf('\n<span class="rr-citation-note">%s</span>', e$description)
  } else ""
  sprintf(
    '::: {.rr-media-citation}\n**%s** · %s\\\n[%s](%s){target="_blank"}\\%s\n:::\n\n',
    e$source, date_fmt, e$title, e$url, desc_html
  )
}

render_podcast_html <- function(e) {
  date_fmt <- format(as.Date(e$date), "%B %d, %Y")
  episode_part <- if (!is.null(e$episode)) sprintf(" · %s", e$episode) else ""
  desc_html <- if (!is.null(e$description)) sprintf("%s ", e$description) else ""
  link_label <- if (grepl("youtube\\.com|youtu\\.be", e$url, ignore.case = TRUE)) "Watch on YouTube" else "Listen"
  sprintf(
    '::: {.rr-podcast-entry}\n**%s**%s · %s\\\n*%s*\\\n%s[[%s](%s){target="_blank"}]\n:::\n\n',
    e$source, episode_part, date_fmt, e$title, desc_html, link_label, e$url
  )
}

render_announcement_html <- function(e) {
  date_fmt <- format(as.Date(e$date), "%B %d, %Y")
  desc_html <- if (!is.null(e$description)) sprintf("\n\n%s", e$description) else ""
  sprintf(
    '::: {.rr-media-citation}\n**%s** · %s\\\n[%s](%s){target="_blank"}\\%s\n:::\n\n',
    e$source, date_fmt, e$title, e$url, desc_html
  )
}

render_section_html <- function(entries, type) {
  filtered <- Filter(function(e) e$type == type, entries)
  if (length(filtered) == 0) {
    cat("<p><em>Entries coming soon.</em></p>\n")
    return(invisible(NULL))
  }
  renderer <- switch(type,
    news         = render_news_html,
    podcast      = render_podcast_html,
    announcement = render_announcement_html
  )
  cat(sapply(filtered, renderer), sep = "")
}
