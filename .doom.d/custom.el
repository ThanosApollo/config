;;; custom.el -*- lexical-binding: t; -*-



(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   '("97db542a8a1731ef44b60bc97406c1eb7ed4528b0d7296997cbb53969df852d6" default))
 '(doc-view-continuous t)
 '(org-agenda-files '("~/Documents/org/agenda.org"))
 '(package-selected-packages '(exwm ##))
 '(warning-suppress-log-types '((erc) (erc)))
 '(warning-suppress-types '((erc) (erc))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 ;;
 ;;Org mode settings
 '(org-level-1 ((t (:inherit outline-1 :height 1.3 :family "Helvetica"))))
 '(org-level-2 ((t (:inherit outline-2 :height 1.2 :family "Hack"))))
 '(org-level-3 ((t (:inherit outline-2 :height 1.2))))
 '(org-level-4 ((t (:inherit outline-2 :height 1.0))))
 '(org-level-5 ((t (:inherit outline-2 :height 1.0))))
 ;; Font
 '(default ((t (:height 100 :family "Hack"))))
 )

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
