;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.
(setq user-full-name "Apo11o"
      user-mail-address "Apo11ongr@proton.me")

;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-unicode-font' -- for unicode glyphs
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;

;; (setq doom-font (font-spec :family "mono" :size 12 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "mono") ; inherits `doom-font''s :size
;;       doom-unicode-font (font-spec :family "Input Mono Narrow" :size 12)
;;       doom-big-font (font-spec :family "Mono" :size 19))
;; ;; If you or Emacs can't find your font, use 'M-x describe-font' to look them
;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)

;;(setq modus-themes-mode-line '(accented boarderless))
;;(setq modus-themes-region '(bg-only))



;(load-theme 'modus-vivendi t)


;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org")


;; Whenever you reconfigure a package, make sure to wrap your config in an
;; `after!' block, otherwise Doom's defaults may override your settings. E.g.
;;
;;   (after! PACKAGE
;;     (setq x y))
;;
;; The exceptions to this rule:
;;
;;   - Setting file/directory variables (like `org-directory')
;;   - Setting variables which explicitly tell you to set them before their
;;     package is loaded (see 'C-h v VARIABLE' to look up their documentation).
;;   - Setting doom variables (which start with 'doom-' or '+').
;;
;; Here are some additional functions/macros that will help you configure Doom.
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;; Alternatively, use `C-h o' to look up a symbol (functions, variables, faces,
;; etc).
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.



;; Default settings
(setq browser-url-browser-function 'browse-url-default-browser)

;; Dired
(use-package dired
  :ensure nil
  :commands (dired dired-jump)
  :bind (("C-x C-j" . dired-jump))
  :config
  (evil-collection-define-key 'normal' dired-mode-map
                               "h" 'dired-up-directory
                               "l" 'dired-find-file))

(custom-set-variables
'(custom-safe-themes
   '("97db542a8a1731ef44b60bc97406c1eb7ed4528b0d7296997cbb53969df852d6" default))
 '(doc-view-continuous t)
 '(org-agenda-files '("~/org/agenda.org"))
 '(package-selected-packages
   '(pdf-tools org-anki anki-connect quelpa-use-package exwm ##))
 '(warning-suppress-log-types '((erc) (erc)))
 '(warning-suppress-types '((color-theme) (erc) (erc))))
(custom-set-faces
'(default ((t (:height 100 :family "hack"))))
 '(org-level-1 ((t (:inherit outline-1 :height 1.3 :family "hack"))))
 '(org-level-2 ((t (:inherit outline-2 :height 1.2 :family "source code pro"))))
 '(org-level-3 ((t (:inherit outline-2 :height 1.2 :family "mono"))))
 '(org-level-4 ((t (:inherit outline-2 :height 1.0))))
 '(org-level-5 ((t (:inherit outline-2 :height 1.0)))))


(defvar my-linum-current-line-number 0)

(setq linum-format 'my-linum-relative-line-numbers)

(defun my-linum-relative-line-numbers (line-number)
  (let ((test2 (1+ (- line-number my-linum-current-line-number))))
    (propertize
     (number-to-string (cond ((<= test2 0) (1- test2))
                             ((> test2 0) test2)))
     'face 'linum)))

(defadvice linum-update (around my-linum-update)
  (let ((my-linum-current-line-number (line-number-at-pos)))
    ad-do-it))
(ad-activate 'linum-update)

;; Theme


;; Elfeed
;;
(global-set-key (kbd "C-c e") 'elfeed)
(global-set-key (kbd "C-c u") 'elfeed-update)
(require 'elfeed)
(use-package elfeed
  :config
  (setq elfeed-search-feed-face ":foreground #fff :weight bold"
        elfeed-feeds (quote
                       (("https://www.gamingonlinux.com/article_rss.php" gaming linux)
                        ("https://hackaday.com/blog/feed/" hackaday linux)
                        ("https://opensource.com/feed" opensource linux)
                        ("https://linux.softpedia.com/backend.xml" softpedia linux)
                        ("https://www.thelancet.com/rssfeed/ebiom_current.xml" medicine ebiom)
                        ("https://www.computerworld.com/index.rss" computerworld linux)
                        ("https://www.networkworld.com/category/linux/index.rss" networkworld linux)
                        ("https://www.techrepublic.com/rssfeeds/topic/open-source/" techrepublic linux)
                        ("https://betanews.com/feed" betanews linux)
                        ("http://lxer.com/module/newswire/headlines.rss" lxer linux)
                        ("https://stallman.org/rss/rss.xml"RichardStallman)))))

(use-package elfeed-goodies
  :init
  (elfeed-goodies/setup)
  :config
  (setq elfeed-goodies/entry-pane-size 0.5))

(defun elfeed-search-format-date (date)
  (format-time-string "%Y-%m-%d %H:%M" (seconds-to-time date)))
(add-hook 'elfeed-show-mode-hook 'visual-line-mode)
(evil-define-key 'normal elfeed-show-mode-map
  (kbd "J") 'elfeed-goodies/split-show-next
  (kbd "K") 'elfeed-goodies/split-show-prev)
(evil-define-key 'normal elfeed-search-mode-map
  (kbd "J") 'elfeed-goodies/split-show-next
  (kbd "K") 'elfeed-goodies/split-show-prev)
