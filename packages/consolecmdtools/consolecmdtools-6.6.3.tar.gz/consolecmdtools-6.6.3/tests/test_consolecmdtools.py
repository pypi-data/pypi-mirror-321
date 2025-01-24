#!/usr/bin/env python3
import sys
import platform
import os
import unittest
import tempfile
from unittest.mock import patch

import FakeOut
import FakeIn
import FakeOs
import FakeErr

test_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)
import consolecmdtools as cct  # noqa

OFFLINE_MODE = True  # Comment this line to run all tests


class test_consolecmdtools(unittest.TestCase):
    """consolecmdtools unit tests"""

    def setUp(self):
        # redirect stdout
        self.console_out = sys.stdout
        self.fakeout = FakeOut.FakeOut()
        sys.stdout = self.fakeout
        # redirect stdin
        self.console_in = sys.stdin
        self.fakein = FakeIn.FakeIn()
        sys.stdin = self.fakein
        # redirect stderr
        self.console_err = sys.stderr
        self.fakeerr = FakeErr.FakeErr()
        sys.stderr = self.fakeerr
        # monkey patch
        self.os_system = os.system
        self.fakeos = FakeOs.FakeOs()
        os.system = self.fakeos.system

    def tearDown(self):
        # clean fakin/out buffer
        self.fakeout.clean()
        self.fakein.clean()
        self.fakeos.clean()
        # set back stdin/out to console
        sys.stdout = self.console_out
        sys.stdin = self.console_in
        os.system = self.os_system

    def test_version(self):
        self.assertTrue(isinstance(cct.__version__, str))

    def test_banner(self):
        expect_word = '################\n#  Test Text   #\n################'
        self.assertEqual(expect_word, cct.banner("Test Text"))

    def test_md5_string(self):
        md5 = cct.md5("Test Text")
        self.assertEqual(md5, 'f1feeaa3d698685b6a6179520449e206')

    def test_md5_int(self):
        md5 = cct.md5(42)
        self.assertEqual(md5, 'a1d0c6e83f027327d8461063f4ac58a6')

    def test_md5_bytes(self):
        md5 = cct.md5(b'Test Text')
        self.assertEqual(md5, 'f1feeaa3d698685b6a6179520449e206')

    def test_md5_file(self):
        filepath = os.path.join(project_dir, "tests", "testfile")
        md5 = cct.md5(filepath)
        self.assertEqual(md5, '02e6b5a02826a57a066bb658cca94c50')

    def test_md5_force_text(self):
        filepath = os.path.join(project_dir, "tests", "testfile")
        md5 = cct.md5(filepath, force_text=True)
        self.assertNotEqual(md5, '02e6b5a02826a57a066bb658cca94c50')

    def test_crc32_string(self):
        crc32 = cct.crc32("Test Text")
        self.assertEqual(crc32, 1739839371)

    def test_crc32_int(self):
        crc32 = cct.crc32(42)
        self.assertEqual(crc32, 841265288)

    def test_crc32_bytes(self):
        crc32 = cct.crc32(b'Test Text')
        self.assertEqual(crc32, 1739839371)

    def test_crc32_file(self):
        filepath = os.path.join(project_dir, "tests", "testfile")
        crc32 = cct.crc32(filepath)
        self.assertEqual(crc32, 602403306)

    def test_crc32_force_text(self):
        filepath = os.path.join(project_dir, "tests", "testfile")
        crc32 = cct.crc32(filepath, force_text=True)
        self.assertNotEqual(crc32, 602403306)

    def test_main_color_rgb_file(self):
        img_file = os.path.join(test_dir, "image.jpg")
        color = cct.main_color(img_file)
        self.assertEqual(color, (226, 175, 106))

    def test_main_color_hex_file(self):
        img_file = os.path.join(test_dir, "image.jpg")
        color = cct.main_color(img_file, triplet='hex')
        self.assertEqual(color, '#E2AF6A')

    @unittest.skipIf(OFFLINE_MODE, 'Offline mode')
    def test_main_color_rgb_url(self):
        img_url = "https://raw.githubusercontent.com/kyan001/PyConsoleCMDTools/main/tests/image.jpg"
        color = cct.main_color(img_url, is_url=True)
        self.assertEqual(color, (226, 175, 106))

    @unittest.skipIf(OFFLINE_MODE, 'Offline mode')
    def test_main_color_hex_url(self):
        img_url = "https://raw.githubusercontent.com/kyan001/PyConsoleCMDTools/main/tests/image.jpg"
        color = cct.main_color(img_url, is_url=True, triplet='hex')
        self.assertEqual(color, '#E2AF6A')

    def test_clear_screen(self):
        cct.clear_screen()
        self.assertTrue(self.fakeos.readline() in 'cls clear')

    def test_get_py_cmd(self):
        result = cct.get_py_cmd()
        self.assertTrue(result in ('py', 'python3'))

    def test_run_cmd(self):
        cct.run_cmd("Test Command")
        self.assertEqual(self.fakeos.readline(), "Test Command")

    def test_read_cmd(self):
        self.assertEqual(cct.read_cmd("echo Test Text").strip(), "Test Text")

    def test_read_cmd_verbose(self):
        cct.read_cmd("echo Test Text", verbose=True)
        self.assertIn("echo Test Text", self.fakeout.readline())
        cct.read_cmd("echo Test Text", verbose=False)
        self.assertEqual(self.fakeout.readline(), None)

    def test_read_cmd_error(self):
        cct.read_cmd("notexist")
        self.assertIn("notexist", self.fakeout.readline())

    def test_is_cmd_exist(self):
        with patch("os.system", new=self.os_system):
            self.assertFalse(cct.is_cmd_exist("notexist"))
            self.assertTrue(cct.is_cmd_exist("ls"))

    def test_install_package_name_str(self):
        result = cct.install_package("_fake_package_name")
        self.assertIn("_fake_package_name", self.fakeout.readline())
        self.assertTrue(result)

    def test_install_package_name_dict(self):
        result = cct.install_package({"Windows": "_fake_package_name", "Darwin": "_fake_package_name", "Linux": "_fake_package_name"})
        self.assertIn("_fake_package_name", self.fakeout.readline())
        self.assertTrue(result)

    def test_install_package_name_wildcard(self):
        result = cct.install_package({"*": "_fake_package_name"})
        self.assertIn("_fake_package_name", self.fakeout.readline())
        self.assertTrue(result)

    def test_install_package_manager_str(self):
        result = cct.install_package("_fake_package_name", manager="pip3")
        self.assertIn("pip3", self.fakeout.readline())
        self.assertTrue(result)

    def test_install_package_manager_notexist(self):
        result = cct.install_package("_fake_package_name", manager="_fake_manager_name")
        self.assertIn("Unsupported", self.fakeout.readline())
        self.assertFalse(result)

    def test_install_package_manager_dict(self):
        result = cct.install_package("_fake_package_name", manager={"Windows": "_fake_manager_name", "Darwin": "_fake_manager_name", "Linux": "_fake_manager_name"})
        self.assertIn("_fake_manager_name", self.fakeout.readline())
        self.assertFalse(result)

    def test_install_package_manager_wildcard(self):
        result = cct.install_package("_fake_package_name", manager={"*": "_fake_manager_name"})
        self.assertIn("_fake_manager_name", self.fakeout.readline())
        self.assertFalse(result)

    def test_get_path_file(self):
        file_path = cct.get_path(__file__)
        self.assertTrue(file_path.endswith("test_consolecmdtools.py"))

    def test_get_path_file_abs(self):
        file_abs = cct.get_path(__file__).abs
        self.assertEqual(file_abs, os.path.abspath(__file__))

    def test_get_path_file_abs_expanduser(self):
        file_abs = cct.get_path("~/.file").abs
        self.assertTrue(os.path.isabs(file_abs))
        self.assertFalse("~" in file_abs)

    def test_get_path_file_basename(self):
        file_basename = cct.get_path(__file__).basename
        self.assertEqual(file_basename, "test_consolecmdtools.py")

    def test_get_path_file_ext(self):
        file_ext = cct.get_path(__file__).ext
        self.assertEqual(file_ext, "py")

    def test_get_path_file_stem(self):
        file_stem = cct.get_path(__file__).stem
        self.assertEqual(file_stem, "test_consolecmdtools")

    def test_get_path_parent(self):
        parent_path = cct.get_path(__file__).parent
        self.assertTrue(parent_path.endswith("tests"))

    def test_get_path_parent_basename(self):
        parent_basename = cct.get_path(__file__).parent.basename
        self.assertEqual(parent_basename, "tests")

    def test_get_path_parent_ext(self):
        parent_ext = cct.get_path(__file__).parent.ext
        self.assertEqual(parent_ext, "")

    def test_get_path_parent_stem(self):
        parent_stem = cct.get_path(__file__).parent.stem
        self.assertEqual(parent_stem, "tests")

    def test_get_path_exists(self):
        path = cct.get_path(__file__)
        self.assertTrue(path.exists)

    def test_get_path_is_dir(self):
        path = cct.get_path(__file__)
        self.assertFalse(path.is_dir)
        self.assertTrue(path.parent.is_dir)

    def test_get_path_is_file(self):
        path = cct.get_path(__file__)
        self.assertTrue(path.is_file)
        self.assertFalse(path.parent.is_file)

    def test_diff_same(self):
        diffs = cct.diff("test", "test")
        self.assertFalse(diffs)

    def test_diff_str(self):
        a, b = "test1", "test2"
        expect_diff = [
            "-test1",
            "+test2"
        ]
        self.assertEqual(cct.diff(a, b), expect_diff)

    def test_diff_meta(self):
        a, b = "test1", "test2"
        expect_diff = [
            "--- <class 'str'>",
            "+++ <class 'str'>",
            "@@ -1 +1 @@",
            "-test1",
            "+test2"
        ]
        self.assertEqual(cct.diff(a, b, meta=True), expect_diff)

    def test_diff_list(self):
        a, b = ["a", "c"], ["b", "c"]
        expect_diff = [
            "-a",
            "+b"
        ]
        self.assertEqual(cct.diff(a, b), expect_diff)

    def test_diff_context(self):
        a, b = ["a", "c"], ["b", "c"]
        expect_diff = [
            "-a",
            "+b",
            " c"
        ]
        self.assertEqual(cct.diff(a, b, context=1), expect_diff)

    def test_diff_file(self):
        a = os.path.join(project_dir, "tests", "testfile")
        b = "This file should not changed too"
        expect_diff = [
            "-This file should not changed",
            "+This file should not changed too"
        ]
        self.assertEqual(cct.diff(a, b), expect_diff)

    def test_diff_files(self):
        a = os.path.join(project_dir, "tests", "testfile")
        b = os.path.join(project_dir, "tests", "testfile2")
        expect_diff = [
            "-This file should not changed",
            "+This file should not changed too"
        ]
        self.assertEqual(cct.diff(a, b), expect_diff)

    def test_diff_force_str(self):
        a = os.path.join(project_dir, "tests", "testfile")
        b = os.path.join(project_dir, "tests", "testfile2")
        self.assertTrue("-{}".format(a) in cct.diff(a, b, force_str=True))

    @unittest.skipIf(OFFLINE_MODE, 'Offline mode')
    def test_update_file(self):
        url = "https://raw.githubusercontent.com/kyan001/PyConsoleCMDTools/main/tests/testfile"
        filepath = os.path.join(project_dir, "tests", "testfile")
        result = cct.update_file(filepath, url)
        expect = "testfile is already up-to-date."
        self.assertFalse(result)
        self.assertIn(expect, self.fakeout.readline())

    def test_read_file(self):
        filepath = os.path.join(project_dir, "tests", "testfile")
        content = cct.read_file(filepath)
        self.assertEqual(content, "This file should not changed\n")

    def test_copy_file(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd) as fdst:
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertFalse(os.path.exists(dst))
            cct.copy_file(src, dst)
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))

    def test_copy_file_copy_false(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd) as fdst:
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertFalse(os.path.exists(dst))
            cct.copy_file(src, dst, copy=False)  # copy should be ignored
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))

    def test_move_file_move(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd) as fdst:  # dst is deleted after creation
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertFalse(os.path.exists(dst))
            cct.move_file(src, dst)
            self.assertFalse(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))

    def test_move_file_copy(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd) as fdst:  # dst is deleted after creation
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertFalse(os.path.exists(dst))
            cct.move_file(src, dst, copy=True)
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))

    def test_move_file_overwrite(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fdst:
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))
            cct.move_file(src, dst, copy=True)
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))
            cct.move_file(src, dst, copy=False)
            self.assertFalse(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))

    def test_move_file_backup(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fdst:
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))
            cct.move_file(src, dst, backup=True)
            self.assertFalse(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))

    def test_move_file_msgout(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc, tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fdst:
                src = fsrc.name
                dst = fdst.name
            self.assertTrue(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))
            cct.move_file(src, dst, msgout=print)
            self.assertFalse(os.path.exists(src))
            self.assertTrue(os.path.exists(dst))
            self.assertIn(src, self.fakeout.readline())
            self.assertIn(dst, self.fakeout.readline())

    def test_move_file_ensure(self):
        with tempfile.TemporaryDirectory() as tmpd:
            with tempfile.NamedTemporaryFile(dir=tmpd, delete=False) as fsrc:
                src = fsrc.name
                dst = os.path.join(tmpd, "dst_folder", "dst_file")
            self.assertFalse(os.path.exists(dst))
            cct.move_file(src, dst, ensure=True)
            self.assertTrue(os.path.exists(dst))

    @unittest.skipIf(OFFLINE_MODE, 'Offline mode')
    def test_ajax_get(self):
        url = "https://yesno.wtf/api"
        param = {"force": "yes"}
        result = cct.ajax(url=url, param=param, method="get")
        answer = result.get("answer")
        self.assertEqual(answer, "yes")

    def test_is_python3(self):
        self.assertEqual(cct.is_python3(), True)

    @unittest.skipUnless(platform.system() == "Windows", 'requires Windows')
    def test_is_admin(self):
        self.assertEqual(cct.is_admin(), False)

    @unittest.skipUnless(platform.system() == "Windows", 'requires Windows')
    def test_runas_admin(self):
        script_path = os.path.join(project_dir, "tests", "test_runas.py")
        self.assertEqual(cct.runas_admin(script_path), True)

    @unittest.skipUnless(platform.system() == "Windows", 'requires Windows')
    def test_runas_admin_error(self):
        with self.assertRaises(FileNotFoundError):
            cct.runas_admin("not-exist.file")

    @unittest.skip('GUI Test skipped.')
    def test_select_path(self):
        self.assertEqual(os.path.dirname(cct.select_path(initialdir=test_dir)).replace("/", "\\"), test_dir)

    def test_bfs_walk(self):
        root = "tests"
        result = [path.name for path in cct.bfs_walk(root)]
        self.assertIn("test_consolecmdtools.py", result)

    def test_get_files(self):  # deprecated
        root = "tests"
        result = cct.get_files(root)
        self.assertIn("DeprecationWarning: Function `get_files` is deprecated, now calling `get_paths` instead.", self.fakeerr.readline())
        self.assertIn(os.path.join(root, "test_consolecmdtools.py"), result)

    def test_get_paths(self):
        root = "tests"
        result = cct.get_paths(root)
        self.assertIn(os.path.join(root, "test_consolecmdtools.py"), result)

    def test_ls_tree(self):
        root = "tests"
        cct.ls_tree(root)
        self.assertIn("test_consolecmdtools.py", self.fakeout.readline())

    def test_resolve_value_any(self):
        self.assertEqual(cct.resolve_value("test"), "test")

    def test_resolve_value_dict(self):
        data = {
            "Windows": "test",
            "Darwin": "test",
            "*": "test"
        }
        self.assertEqual(cct.resolve_value(data), "test")



if __name__ == '__main__':
    # ONLY_MOVE_FILE = True  # Comment this line to run all tests
    if "ONLY_MOVE_FILE" in locals():
        suite = unittest.TestSuite()
        suite.addTests(test_consolecmdtools(test) for test in [
            'test_move_file_move',
            'test_move_file_copy',
            'test_move_file_overwrite',
            'test_move_file_backup',
            'test_move_file_msgout',
        ])
        unittest.TextTestRunner().run(suite)
    else:
        unittest.main(verbosity=2, exit=False)  # print more info, no sys.exit() called.
