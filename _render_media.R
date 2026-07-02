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
    href <- if (!is.null(e$landing_url)) {
      e$landing_url
    } else if (!is.null(e$id)) {
      sprintf("public_media.html#%s", e$id)
    } else {
      "public_media.html"
    }
    title_tag <- sprintf('<a class="rr-media-title" href="%s">%s</a>', href, display_title)
    sprintf('<div class="rr-media-item">\n  <div class="rr-media-meta">%s</div>\n  %s\n</div>',
      date_fmt, title_tag)
  })
  cat(paste(c(
    '<section class="rr-media-strip">',
    items,
    '  <a class="rr-media-see-all" href="public_media.html">View all media &rarr;</a>',
    '</section>'
  ), collapse = "\n"))
}

# ── Full media page renderers ─────────────────────────────────────

render_news_html <- function(e) {
  date_fmt <- format(as.Date(e$date), "%B %d, %Y")
  id_attr  <- if (!is.null(e$id)) sprintf("#%s ", e$id) else ""
  desc_html <- if (!is.null(e$description)) {
    sprintf('\n<span class="rr-citation-note">%s</span>', e$description)
  } else ""
  sprintf(
    '::: {%s.rr-media-citation}\n**%s** · %s\\\n[%s](%s){target="_blank"}\\%s\n:::\n\n',
    id_attr, e$source, date_fmt, e$title, e$url, desc_html
  )
}

render_podcast_html <- function(e) {
  date_fmt     <- format(as.Date(e$date), "%B %d, %Y")
  id_attr      <- if (!is.null(e$id)) sprintf("#%s ", e$id) else ""
  episode_part <- if (!is.null(e$episode)) sprintf(" · %s", e$episode) else ""
  desc_html    <- if (!is.null(e$description)) sprintf("%s ", e$description) else ""
  link_label   <- if (grepl("youtube\\.com|youtu\\.be", e$url, ignore.case = TRUE)) "Watch on YouTube" else "Listen"
  sprintf(
    '::: {%s.rr-podcast-entry}\n**%s**%s · %s\\\n*%s*\\\n%s[[%s](%s){target="_blank"}]\n:::\n\n',
    id_attr, e$source, episode_part, date_fmt, e$title, desc_html, link_label, e$url
  )
}

render_announcement_html <- function(e) {
  date_fmt  <- format(as.Date(e$date), "%B %d, %Y")
  id_attr   <- if (!is.null(e$id)) sprintf("#%s ", e$id) else ""
  imgs         <- if (!is.null(e$images)) e$images else if (!is.null(e$image)) list(e$image) else list()
  has_image    <- length(imgs) > 0
  multi        <- length(imgs) > 1
  thumb_class  <- if (isTRUE(e$thumb_borderless)) ".rr-announcement-thumb .rr-thumb-borderless" else ".rr-announcement-thumb"

  title_html <- if (!is.null(e$url)) {
    sprintf('[%s](%s){target="_blank"}', e$title, e$url)
  } else e$title

  desc_part <- if (!is.null(e$description)) {
    if (has_image) sprintf("\\\n%s", e$description) else sprintf("\n\n%s", e$description)
  } else ""

  if (!has_image) {
    sprintf('::: {%s.rr-media-citation}\n**%s** · %s\\\n%s%s\n:::\n\n',
      id_attr, e$source, date_fmt, title_html, desc_part)
  } else {
    group_id <- paste0("ann-", gsub("[^a-z0-9]", "", tolower(e$date)))
    main_img <- sprintf('![](%s){.lightbox %s group="%s"}', imgs[[1]], thumb_class, group_id)

    image_block <- if (multi) {
      hidden_imgs <- paste(sapply(imgs[-1], function(img) {
        sprintf('![](%s){.lightbox group="%s"}', img, group_id)
      }), collapse = "\n\n")
      paste0('::: {.rr-thumb-stack}\n', main_img,
             '\n\n::: {.rr-thumb-hidden}\n', hidden_imgs, '\n:::\n:::')
    } else {
      main_img
    }

    # 4-colon outer fence so inner ::: fences don't close it prematurely
    sprintf(':::: {%s.rr-media-citation .rr-has-thumb}\n**%s** · %s\\\n%s%s\n\n%s\n::::\n\n',
      id_attr, e$source, date_fmt, title_html, desc_part, image_block)
  }
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
